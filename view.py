from tkinter import Tk, Label,ttk




def create_main_view():
    main_view = Tk()
    message_selector = create_message_selector(main_view,0,0)
    main_view.mainloop()

def create_message_selector(view,pos_x,pos_y):
    messages = ['east_1', 'east_2', 'east_3', 'east_4', 'east_5', 'west_1', 'west_2', 'west_3', 'west_4']
    message_selector_label = Label(view,
                        text="Select message:")
    message_selector_label.grid(column=pos_x, row=pos_y)
    message_selector = ttk.Combobox(view,
                                values=messages,
                                state="readonly")

    message_selector.grid(column=pos_x, row=pos_y+1)

    def message_selector_callback(event):
        print("Message selected selected" + message_selector.get()+" "+ str(event))

    message_selector.bind("<<ComboboxSelected>>", message_selector_callback)
    message_selector.current(0)


