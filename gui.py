import tkinter as tk
import main as cli


def token_submit(token_var, token_tk):
    token = token_var.get()
    with open("token.json", "w") as tokenfile:
        tokenfile.write(token)
    token_var.set("")
    token_tk.withdraw()
    # send_email_window()
    open_inbox_window()


def token_window():
    token_tk = tk.Tk()
    frame = tk.Frame(token_tk)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    token_label = tk.Label(frame, text="Token:")
    token_label.pack(fill="x", expand=True)

    token_var = tk.StringVar()
    token_entry = tk.Entry(frame, textvariable=token_var)
    token_entry.pack(fill="x", expand=True)
    token_entry.focus()

    sub_btn = tk.Button(
        frame, text="Submit", command=lambda: token_submit(token_var, token_tk)
    )
    sub_btn.pack(fill="x")

    token_tk.mainloop()


def send_email_submit(from_var, to_var, subject_var, body_text):
    cli.gmail_send_message(
        from_var.get(), to_var.get(), subject_var.get(), body_text.get("1.0", "end-1c")
    )


def open_inbox_submit():
    subject, sender, body = cli.receive_messages(10)
    print(subject, sender, body, "\n-----------------------------\n", sep="\n")


def open_threads_submit():
    pass


def open_inbox_window():
    open_inbox_tk = tk.Toplevel()
    open_inbox_tk.title("PyMail")
    T = Text(root, height=5, width=80)
    test_text = tk.Label(open_inbox_tk, text="test")
    inbox_emails = tk.Label(open_inbox_tk, text="Inbox emails")
    test_text.pack()
    inbox_emails.pack()
    open_inbox_tk.mainloop()
    #
    # to_label = tk.Label(open_inbox_tk, text="To:")
    # from_label = tk.Label(open_inbox_tk, text="From:")
    # subject_label = tk.Label(open_inbox_tk, text="Subject:")
    # body_label = tk.Label(open_inbox_tk, text="Body:")
    #
    # to_var = tk.StringVar()
    # from_var = tk.StringVar()
    # subject_var = tk.StringVar()
    #
    # to_entry = tk.Entry(send_email_tk, textvariable=to_var)
    # from_entry = tk.Entry(send_email_tk, textvariable=from_var)
    # subject_entry = tk.Entry(send_email_tk, textvariable=subject_var)
    # body_text = tk.Text(send_email_tk, height=5, width=30)
    #
    # sub_btn = tk.Button(send_email_tk, text='Submit', command=lambda: send_email_submit(from_var, to_var, subject_var, body_text))
    #
    # to_label.grid(row=0, column=0, pady=2)
    # from_label.grid(row=1, column=0, pady=2)
    # subject_label.grid(row=2, column=0, pady=2)
    # body_label.grid(row=3, column=0, pady=2)
    #
    # to_entry.grid(row=0, column=1, pady=2)
    # from_entry.grid(row=1, column=1, pady=2)
    # subject_entry.grid(row=2, column=1, pady=2)
    # body_text.grid(row=3, column=1, pady=2)
    #
    # sub_btn.grid(row=4, column=1, pady=2)
    #
    # inbox_btn.grid(row=10, column=1, pady=2)
    # threads_btn.grid(row=11, column=1, pady=2)


def send_email_window():
    send_email_tk = tk.Toplevel()
    send_email_tk.title("PyMail")

    to_label = tk.Label(send_email_tk, text="To:")
    from_label = tk.Label(send_email_tk, text="From:")
    subject_label = tk.Label(send_email_tk, text="Subject:")
    body_label = tk.Label(send_email_tk, text="Body:")

    to_var = tk.StringVar()
    from_var = tk.StringVar()
    subject_var = tk.StringVar()

    to_entry = tk.Entry(send_email_tk, textvariable=to_var)
    from_entry = tk.Entry(send_email_tk, textvariable=from_var)
    subject_entry = tk.Entry(send_email_tk, textvariable=subject_var)
    body_text = tk.Text(send_email_tk, height=5, width=30)

    sub_btn = tk.Button(
        send_email_tk,
        text="Submit",
        command=lambda: send_email_submit(from_var, to_var, subject_var, body_text),
    )
    inbox_btn = tk.Button(
        send_email_tk, text="Open Inbox", command=lambda: open_inbox_submit()
    )
    threads_btn = tk.Button(
        send_email_tk, text="Open Threads", command=lambda: open_threads_submit()
    )

    to_label.grid(row=0, column=0, pady=2)
    from_label.grid(row=1, column=0, pady=2)
    subject_label.grid(row=2, column=0, pady=2)
    body_label.grid(row=3, column=0, pady=2)

    to_entry.grid(row=0, column=1, pady=2)
    from_entry.grid(row=1, column=1, pady=2)
    subject_entry.grid(row=2, column=1, pady=2)
    body_text.grid(row=3, column=1, pady=2)

    sub_btn.grid(row=4, column=1, pady=2)

    inbox_btn.grid(row=10, column=1, pady=2)
    threads_btn.grid(row=11, column=1, pady=2)
    send_email_tk.mainloop()


def main():
    token_window()


if __name__ == "__main__":
    main()
