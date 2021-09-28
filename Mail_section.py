from ast import literal_eval
from getpass import getpass
from smtplib import SMTP

from data_types import convert, log, mail
from file_operation import File
from operations import (
    change_status,
    clear_screen,
    get_date_time,
    is_connected,
    is_input_kill,
    is_mail_id,
    write_log,
)
from Reminder_section import reminder_section

__name__ = "__mail_section"


class mail_section(change_status):
    """
    For sending E-Mail
    """

    def __init__(self) -> None:
        super().__init__()
        self.__mail_data_path = "Data/mail_data.json"
        self.__mail_file = File(file_location=self.__mail_data_path)

    def new_mail(self) -> None:
        """
        To add Mail from main section
        """
        self.__new_mail_read_data(mail_type="none")

    def __new_mail_read_data(self, mail_type: str) -> None:
        """
        Read data for sending new mail
        """
        try:
            if mail_type == "new":
                while True:
                    from_address = input("From Address : ")
                    if is_input_kill(data=from_address):
                        return
                    if not is_mail_id(mail_id=from_address, mail_site="gmail"):
                        continue
                    break
            else:
                from_address = ""
            while True:
                to_address = input("To Address : ")
                if is_input_kill(data=from_address):
                    return
                if not is_mail_id(mail_id=from_address):
                    continue
                break
            password = getpass("Password : ")
            # do encryption here

            subject = input("Subject : ")
            body = input("Body : ")
            self.__configure_mail_phase_1(
                from_address=from_address,
                to_address=to_address,
                subject=subject,
                body=body,
                password=password,
            )
        except Exception as e:
            print(f"Mail_section > __new_mail_read_data - {e}")

    def __configure_mail_phase_1(
        self, from_address: str, to_address: str, password: str, subject: str, body: str
    ) -> None:
        """
        Configure mail for sending
        """
        try:
            mail_list = self.__mail_file.read_data()
            if len(mail_list) == 0:
                mail_id = 0
            else:
                mail_id = convert(file_data=mail_list[-1]).to_mail().get_id()
            mail_id += 1
            new_mail = mail(
                mail_id=mail_id,
                from_address=from_address,
                to_address=to_address,
                mail_subject=subject,
                mail_body=body,
                password=password,
            )
            new_mail = self.__configure_mail_phase_2(new_mail=new_mail)
            self.__mail_file.append_one_data(data_to_append=new_mail)
            self.__change_mail_status()
        except Exception as e:
            print(f"Mail_section > __configure_mail_phase_1 - {e}")

    def __configure_mail_phase_2(self, new_mail: mail) -> mail:
        try:
            if is_connected():
                return_data = self.__send_mail(new_mail=new_mail)
                if return_data == True:
                    print("Success")
                    new_mail.set_status()
                else:
                    print("unable to send email")
                    if str(return_data).__contains__("not accepted"):
                        print("invalid email or password")
                        # generating a auto reminder saying an error found while sending mail
                        reminder_section().auto_reminder(
                            reminder_data=f"Mail sending error. ID : {new_mail.get_id()} error : Invalid email or password",
                            reminder_type="error",
                        )
                    else:
                        # generating a auto reminder saying an error found while sending mail
                        reminder_section().auto_reminder(
                            reminder_data=f"Mail sending error. ID : {new_mail.get_id()} error : {return_data}",
                            reminder_type="error",
                        )
                        new_mail.set_status(status="error")
                        new_mail.set_remark(remark=return_data)
            else:
                print(
                    "no internet connection.\nEmail will be sent when system goes online next"
                )
            return new_mail
        except Exception as e:
            print(f"Mail_section > __configure_mail_phase_2 - {e}")

    def __send_mail(self, new_mail: mail) -> bool:
        """
        tries to send the mail
        """
        try:
            password = new_mail.get_password()
            print(password)
            server = SMTP("smtp.gmail.com:587")
            server.ehlo()
            server.starttls()
            server.login(new_mail.get_from_address(), password)
            message = f"Subject : {new_mail.get_subject()}  \n\n\n{new_mail.get_body()}"
            body = new_mail.get_body()
            server.sendmail(
                new_mail.get_from_address(), new_mail.get_to_address(), message, body
            )
            server.quit()
            return True
        except Exception as e:
            # print(f"Mail_section > __send_mail - {e}")
            return e

    def __send_pending_mail(self) -> None:
        """
        try to send currently pending mails
        """
        try:
            if is_connected():
                mail_list = self.__mail_file.read_data()
                for item in mail_list:
                    item_copy = convert(file_data=item).to_mail()
                    if not item_copy.is_completed():
                        print(
                            f"trying to send mail targeted to {item_copy.get_to_address()} from {item_copy.get_from_address()}"
                        )
                        item_copy_2 = self.__configure_mail_phase_2(new_mail=item_copy)
                        if not item_copy == item_copy_2:
                            mail_index = mail_list.index(item)
                            mail_list[mail_index] = item_copy_2.to_string()
                self.__mail_file.rewrite_entire_data(file_data=mail_list)
            else:
                print("Internet connection is not available \n")

        except Exception as e:
            print(f"Mail_section > __send_pending_mail - {e}")

    def show_mail(self) -> None:
        """
        list pending mails, for access from main function
        """
        self.__show_mail(user_input="show")

    def __show_mail(self, user_input: str) -> None:
        """
        list the mails in the list
        """
        try:
            user_input_list = user_input.split()
            mail_list = self.__mail_file.read_data()
            if len(mail_list) == 0:
                print("No mail found")
                return
            if len(user_input_list) == 1 or user_input_list[1] in ["pending", "pend"]:
                if self._change_status__get_status().get_mail_pending_status():
                    mail_status = "pending"
                else:
                    print("No pending mail found")
                    return
            elif user_input_list[1] in ["completed", "comp"]:
                mail_status = "completed"
            elif user_input_list[1] in ["error"]:
                mail_status = "error"
            elif user_input_list[1] == "all":
                for item in mail_list:
                    convert(file_data=item).to_mail().show()
                return
            else:
                print("Incorrect input")
                return
            for item in mail_list:
                flag = True
                item_copy = convert(file_data=item).to_mail()
                if item_copy.get_status() == mail_status:
                    flag = False
                    item_copy.show()
            if flag:
                print("No mail found")
        except Exception as e:
            print(f"Mail_section > __show_mail - {e}")

    def delete_mail(self, user_input: str) -> None:
        """
        To delete a mail as completed from main section
        """
        self.__delete_mail_read_data(user_input=user_input)

    def __delete_mail_read_data(self, user_input: str) -> None:
        """
        Read reminder ID of the reminder which is to deleted
        """
        try:
            if user_input.split()[1] == "all":
                self.__delete_all()
                return
            try:
                mail_id = literal_eval(user_input.split()[-1])
                if type(mail_id) == int:
                    pass
            except Exception:
                try:
                    while True:
                        mail_id = input("Mail ID : ")
                        if not is_input_kill(data=user_input):
                            if type(literal_eval(mail_id)) == int:
                                break
                        else:
                            return
                except Exception:
                    pass
            self.__delete_mail(mail_id=int(mail_id))
        except Exception as e:
            print(f"Mail_section > __delete_mail_read_data - {e}")

    def __delete_all(self) -> None:
        """
        clear all mails in the list
        """
        try:
            if self._change_status__get_status().get_mail_pending_status():
                if not input(
                    "There are mails yet to send,\nDelete all ? (y/n)"
                ).lower() in ["yes", "y"]:
                    return
            self.__mail_file.empty_file()
            print("All mail cleared from list")
        except Exception as e:
            print(f"Mail_section > __delete_all - {e}")

    def __delete_mail(self, mail_id: int) -> None:
        """
        Delete mail from list
        """
        try:
            mail_list = self.__mail_file.read_data()
            for item in mail_list:
                item_copy = convert(file_data=item).to_mail()
                if item_copy.get_id() == int(mail_id):
                    if not item_copy.is_completed():
                        if input("Yet to send.Delete?(y/n) : ").lower() in [
                            "yes",
                            "y",
                        ]:
                            if not self.__mail_file.delete_one_data(
                                file_data=mail_list, data_to_delete=item
                            ):
                                print("Unable to delete data")
                                return
                    break
            else:
                print("No mail found with given mail ID")
            print("Deleted Successfully")
            self.__change_mail_status()
        except Exception as e:
            print(f"Mail_section > __delete_mail - {e}")

    def __pending_mail_count(self) -> int:
        """
        Return the no of pending mail
        """
        try:
            mail_count = 0
            for item in self.__mail_file.read_data():
                if not convert(file_data=item).to_mail().is_completed():
                    mail_count += 1
            return mail_count
        except Exception as e:
            print(f"Mail_section > __pending_mail_count - {e}")

    def __is_mail_pending(self) -> bool:
        """
        Return if mail is pending of not
        """
        try:
            return self._change_status__get_status().get_mail_pending_status()
        except Exception as e:
            print(f"Mail_section > __is_mail_pending - {e}")

    def __change_mail_status(self) -> None:
        """
        change mail status like, is mail pending and if yes how many
        """
        current_status = self._change_status__get_status()
        mail_count = self.__pending_mail_count()
        if mail_count:
            current_status.set_mail_pending_status(mail_status=True)
        else:
            current_status.set_mail_pending_status(mail_status=False)
        current_status.set_mail_pending_count(mail_count=mail_count)
        self._change_status__write_status_to_file(current_status=current_status)

    def startup_mail_check(self) -> None:
        try:
            current_status = self._change_status__get_status()
            if current_status.get_mail_pending_status():
                if is_connected():
                    print(
                        f"There is {current_status.get_mail_pending_count()} pending mails"
                    )
                    print("Attempting to send pending mail(s). \n Please wait")
                    self.__send_pending_mail()
                else:
                    print(
                        f"There are {self.__pending_mail_count()} pending mail(s) \n System will try to send when Internet Connection is available"
                    )
        except Exception as e:
            print(f"Mail_section > startup_mail_check - {e}")

    def __mail_help(self) -> None:
        """
        Show command list related to Mail section
        """
        print(
            """
            -> send             Send new email
            -> send new         send email from user's mail
            -> show [type]      To check email list
            -> pending          To check if emails are pending
            -> clear [type]     Clear emails from list
        """
        )

    def user_section(self) -> bool:
        print("use break or stop to quit Email section")
        while True:
            try:
                input_list = []
                user_input = input(">>> ").lower()
                input_list.append(
                    log(
                        user_input=user_input, section="mail", date_time=get_date_time()
                    )
                )
                user_input_list = user_input.split()
                if user_input == "send":
                    self.__new_mail_read_data(mail_type="none")
                elif user_input == "send new":
                    self.__new_mail_read_data(mail_type="new")
                elif user_input in ["send pend", "send pending"]:
                    if is_connected():
                        if self._change_status__get_status().get_mail_pending_status():
                            self.__send_pending_mail()
                        else:
                            print("No Pending mail found")
                    else:
                        print("No Internet Connection")
                elif user_input == "pending":
                    print(f"There are {self.__pending_mail_count()} pending mails")
                elif user_input_list[0] == "show":
                    self.__show_mail(user_input=user_input)
                elif user_input_list[0] in ["del", "delete"]:
                    self.__delete_mail_read_data(user_input=user_input)
                elif user_input in ["status"]:
                    change_status().show_status()
                elif user_input in ["kill", "stop", "break"]:
                    return False
                elif user_input in ["help", "commands"]:
                    self.__mail_help()
                elif user_input in ["quit", "exit"]:
                    return True
                elif user_input in ["clear"]:
                    clear_screen()
                else:
                    print("Incorrect input")
            except Exception:
                pass
            finally:
                write_log(data_list=input_list)


if __name__ == "__mail_section":
    pass
