from tkinter import *
from PIL import Image ,ImageTk

class Periodic_table:
    detail = ["Name of Element", "Symbol of Element", "Period Number ", "Group Number", "Atomic Number", "Mass number",
              "Type", "Electronegativity\n(KJ/mol)", "Ionization energy\n(KJ/mol)", "Electron affinity\n(KJ/mol)",
              "State"]
    range_details = {1: 4, 2: 5, 3: 7, 4: 8, 5: 9, 6: 6, 7: 10}
    img_folders = ["presentation", "pure_elements", "uses", "properties"]

    def make_periodic_table():
        """importing data from text file and making list of all list elements"""
        Table = open("Periodic_Table.txt", "r")
        periodic_table = []
        for element in Table:
            element = element.rstrip()
            element = element.split(",")
            periodic_table.append(element)
        Table.close()
        return periodic_table

    periodic_table = make_periodic_table()
    def __init__(self):
        """Main window opens after starting"""

        ### Creating tkinter window
        self.window = Toplevel()
        self.window.title("CODE ATOM")
        self.window.configure(bg='#CCFFE5')  ## background colour of window
        self.window.resizable(0, 0)
        self.window.minsize(350, 500)  ### defining minimum size of window width=350,height=500

        ## Creating frame for putting all labels and buttons in representable style
        self.topframe = Frame(self.window, bd=2, relief=SUNKEN, bg='#66FFB2')
        self.topframe.pack()
        self.centerframe = Frame(self.window, bd=2, relief=SUNKEN, bg='#CCCCFF')
        self.centerframe.pack()
        self.root = Frame(self.window, bd=2, relief=SUNKEN,bg="#FFCCCC")
        self.root.pack()

        ### main label and buttons for main window
        self.mode = Label(self.topframe, text="Information of elements in periodic table", font=("Times New Roman", 15), border=5,relief="raised")
        self.mode.grid(row="0", column="0", columnspan="10", padx=10, pady=10)
        self.single = Button(self.topframe, text="To quer single \nelement/period/group", anchor=W, command=lambda:self.single_properties())
        self.single.grid(row="2", column="0", pady=10, padx=5)
        self.range_elem = Button(self.topframe, text="To quer a range \nof elements", anchor=E, command=lambda:self.Range_properties())
        self.range_elem.grid(row="2", column="9", pady=5, padx=5)



    def single_properties(self):
        """Buttons for single element """
        ## creating buttons and call the functions on clicking button
        self.name_button = Button(self.centerframe, text="Name of Element", command=lambda:self.Name_of_Element())
        self.name_button.grid(row="3", column="0", padx=5, pady=5)
        self.symbol_button = Button(self.centerframe, text="Symbol of Element", command=lambda:self.Symbol())
        self.symbol_button.grid(row="3", column="1", padx=5, pady=5)
        self.period_button = Button(self.centerframe, text="Period Number\nof Table(1-7)", command=lambda:self.Period())
        self.period_button.grid(row="3", column="2", padx=5, pady=5)
        self.group_button = Button(self.centerframe, text="Group Number\nof Table(1-18)", command=lambda:self.Group())
        self.group_button.grid(row="3", column="3", padx=5, pady=5)
        self.Atomic_no_button = Button(self.centerframe, text="Atomic Number\nof Element", command=lambda:self.Atomic_no())
        self.Atomic_no_button.grid(row="3", column="4", padx=5, pady=5)

    def Name_of_Element(self):
        """Creating button for name of element and call the function on click"""

        self.button = "single"
        self.values = [i[0] for i in Periodic_table.periodic_table]  ## getting list of names from periodic table
        self.variable1 = StringVar()  ## defining variable
        self.variable1.set(self.values[0])  ## setting default value of variable
        self.name = OptionMenu(self.centerframe, self.variable1, *self.values,command=self.pro_clicked)  ## button having menu  and call the function
        self.name.grid(row="4", column="0", padx=5, pady=5)

    def Symbol(self):
        "Creating button for symbol of element and call the function on click"

        self.button = "single"
        self.values = [i[1] for i in Periodic_table.periodic_table]  ## getting list of symbol from periodic table
        self.variable1 = StringVar()  ## defining variable
        self.variable1.set(self.values[0])  ## setting default value of variable
        self.symbol = OptionMenu(self.centerframe, self.variable1, *self.values,command=self.pro_clicked)  ## button having menu  and call the function
        self.symbol.grid(row="4", column="1", padx=5, pady=5)

    def Period(self):
        """Creating button for all elements of period number selected and call the function on click"""

        self.button = "Period"
        self.values = [1, 2, 3, 4, 5, 6, 7]  ## list of all period numbers
        self.variable1 = IntVar()  ## defining variable
        self.variable1.set(self.values[0])  ## setting default value of variable
        self.period = OptionMenu(self.centerframe, self.variable1, *self.values,command=self.pro_clicked)  ## button having menu  and call the function
        self.period.grid(row="4", column="2", padx=5, pady=5)

    def Group(self):
        """Creating button for all elements of group number selected and call the function on click"""

        self.button = "Group"
        self.values = [i for i in range(1, 19)]  ###list of all group numbers
        self.variable1 = IntVar()  ## defining variable
        self.variable1.set(self.values[0])  ## setting default value of variable
        self.period = OptionMenu(self.centerframe, self.variable1, *self.values,command=self.pro_clicked)  ## button having menu  and call the function
        self.period.grid(row="4", column="3", padx=5, pady=5)

    def Atomic_no(self):
        """Creating button for atomic number of element and call the function on click"""

        self.button = "single"
        self.values = [i[4] for i in Periodic_table.periodic_table]  ## getting list of atomic number from periodic table
        self.variable1 = StringVar()  ## defining variable
        self.variable1.set(self.values[0])  ## setting default value of variable
        self.symbol = OptionMenu(self.centerframe, self.variable1, *self.values,command=self.pro_clicked)  ## button having menu  and call the function
        self.symbol.grid(row="4", column="4", padx=5, pady=5)


    def Range_properties(self):
        """buttons for range of elements"""
        ## creating buttons and call the functions on clicking button
        self.atomic_button = Button(self.root, text="Range of atomic number", command=lambda:self.atm_ranges())
        self.atomic_button.grid(row="6", column="0", padx=5, pady=5)
        self.mass_button = Button(self.root, text="Range of Mass number", command=lambda:self.mass())
        self.mass_button.grid(row="6", column="1", padx=5, pady=5)
        self.electroneg_button = Button(self.root, text="Range of Electronegativity\n(KJ/mol)", command=lambda:self.EN_ranges())
        self.electroneg_button.grid(row="6", column="2", padx=5, pady=5)
        self.ioniz_button = Button(self.root, text="Range of Ionization energy\n(KJ/mol))", command=lambda:self.IE_ranges())
        self.ioniz_button.grid(row="6", column="3", padx=5, pady=5)
        self.elec_aff_button = Button(self.root, text="Range of Electron affinity\n(KJ/mol)", command=lambda:self.EA_ranges())
        self.elec_aff_button.grid(row="6", column="4", padx=5, pady=5)
        self.type_button = Button(self.root, text="Type(Metal/\nMetalloid/Non-Metal)", command=lambda:self.TyPe())
        self.type_button.grid(row="6", column="5", padx=5, pady=5)
        self.state_button = Button(self.root, text="State", command=lambda:self.State())
        self.state_button.grid(row="6", column="6", padx=5, pady=5)

    def atm_ranges(self):
        """Creating button for range of atomic numbers of element and call the function on click"""

        self.ranges = "Atomic_no"
        self.range_Atom = IntVar()
        self.options = [("1-30", 0), ("30-60", 1), ("60-90", 2), ("90-118", 3)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_Atom, value=r_value,command=lambda: self.range_clicked(self.range_Atom.get())).grid(row=f"{rows}", column="0", padx=5, pady=5)
            rows += 1

    def mass(self):
        """Creating mass button for range of mass numbers of element and call the function on click"""

        self.ranges = "mass"
        self.range_mass = IntVar()
        self.options = [("1-75", 0), ("75-150", 1), ("150-225", 2), ("225-300", 3)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_mass, value=r_value,command=lambda: self.range_clicked(self.range_mass.get())).grid(row=f"{rows}", column="1", padx=5, pady=5)
            rows += 1

    def EN_ranges(self):
        """Creating electronegativity button for range of electronegativity of element and call the function on click"""

        self.ranges = "Electronegativity"
        self.range_EN = IntVar()
        self.options = [("0-1", 0), ("1-2", 1), ("2-3", 2), ("N/A", 3)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_EN, value=r_value,command=lambda: self.range_clicked(self.range_EN.get())).grid(row=f"{rows}", column="2", padx=5, pady=5)
            rows += 1

    def IE_ranges(self):
        """Creating ionization energy button for range of ionization energy of element and call the function on click"""

        self.ranges = "Ionization Energy"
        self.range_IE = IntVar()
        self.options = [("100-500", 0), ("500-1000", 1), ("1000-1500", 2), ("N/A", 3)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_IE, value=r_value,command=lambda: self.range_clicked(self.range_IE.get())).grid(row=f"{rows}", column="3", padx=5, pady=5)
            rows += 1

    def EA_ranges(self):
        """Creating electron affinity button for range of electron affinity of element and call the function on click"""

        self.ranges = "Electron Affinity"
        self.range_EA = IntVar()
        self.options = [("0-100", 0), ("100-250", 1), ("250-400", 2), ("N/A", 3)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_EA, value=r_value,command=lambda: self.range_clicked(self.range_EA.get())).grid(row=f"{rows}", column="4", padx=5, pady=5)
            rows += 1

    def TyPe(self):
        """Creating type button for elements having same type and call the function on click"""
        self.ranges = "Type"
        self.range_Type = IntVar()
        self.options = [("Metal", 0), ("Non-Metal", 1), ("Metalloid", 2)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_Type, value=r_value,command=lambda: self.range_clicked(self.range_Type.get())).grid(row=f"{rows}", column="5", padx=5, pady=5)
            rows += 1

    def State(self):
        """Creating state button for elements having same state and call the function on click"""
        self.ranges = "State"
        self.range_State = IntVar()
        self.options = [("Solid", 0), ("Liquid", 1), ("Gas", 2)]
        rows = 7
        for text, r_value in self.options:  ## buttons having options  and call the function
            Radiobutton(self.root, text=text, variable=self.range_State, value=r_value,command=lambda: self.range_clicked(self.range_State.get())).grid(row=f"{rows}", column="6", padx=5,pady=5)
            rows += 1
    def property_root(self):
        """Creating root for property diplay"""
        self.prop_root = Toplevel()  ## creating window for displaying properties
        self.prop_root.configure(bg='sky blue')
        self.propframe = Frame(self.prop_root, bd=2, relief=SUNKEN, bg='sky blue')  ## creating frame for property root
        self.propframe.pack()
    def pro_clicked(self,value):
        """function if any of button of single property click and displaying its output"""
        self.property_root()


        if self.button == "single":
            self.click = "No"
            self.item_index = self.values.index(value)
            self.selected = [Periodic_table.periodic_table[self.item_index]]
            self.imageDisplay(self.item_index)
        if self.button == "Period":
            self.click = "yes"
            self.selected = [i for i in Periodic_table.periodic_table if i[2] == str(value)]
        if self.button == "Group":
            self.click = "yes"
            self.selected = [i for i in Periodic_table.periodic_table if i[3] == str(value)]
        ## calling displaying functions
        self.display_properties(5, self.propframe)
        self.display_prop1(6, self.selected)

    def range_clicked(self,value1):
        """function if any of button of range properties click and displaying its output"""
        self.property_root()

        if self.ranges == "Atomic_no":
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if 1 <= float(i[Periodic_table.range_details[1]]) <= 30]
            elif value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if 30 <= float(i[Periodic_table.range_details[1]]) <= 60]
            elif value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if 60 <= float(i[Periodic_table.range_details[1]]) <= 90]
            else:
                self.range_list = [i for i in Periodic_table.periodic_table if 90 <= float(i[Periodic_table.range_details[1]]) <= 118]
        elif self.ranges == "mass":
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if 1 <= float(i[Periodic_table.range_details[2]]) <= 75]
            elif value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if 75 <= float(i[Periodic_table.range_details[2]]) <= 150]
            elif value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if 150 <= float(i[Periodic_table.range_details[2]]) <= 225]
            else:
                self.range_list = [i for i in Periodic_table.periodic_table if 225 <= float(i[Periodic_table.range_details[2]]) <= 300]
        elif self.ranges == "Electronegativity":
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[3]] != "N/A" if 0 <= float(i[Periodic_table.range_details[3]]) <= 1]
            elif value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[3]] != "N/A" if 1 <= float(i[Periodic_table.range_details[3]]) <= 2]
            elif value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[3]] != "N/A" if  2 <= float(i[Periodic_table.range_details[3]]) <= 3]
            else:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[3]] == "N/A"]
        elif self.ranges == "Ionization Energy":
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[4]] != "N/A" if 300 <= float(i[Periodic_table.range_details[4]]) <= 500]
            elif value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[4]] != "N/A" if 500 <= float(i[Periodic_table.range_details[4]]) <= 1000]
            elif value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[4]] != "N/A" if 1000 <= float(i[Periodic_table.range_details[4]]) <= 1500]
            else:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[4]] == "N/A"]
        elif self.ranges == "Electron Affinity":
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[5]] != "N/A" if 0 <= float(i[Periodic_table.range_details[5]]) <= 100]
            elif value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[5]] != "N/A" if 100 <= float(i[Periodic_table.range_details[5]]) <= 250]
            elif value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[5]] != "N/A" if  250 <= float(i[Periodic_table.range_details[5]]) <= 400]
            else:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[5]] == "N/A"]
        elif self.ranges == "Type":
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[6]] == "Metal"]
            if value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[6]] == "Non Metal"]
            if value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[6]] == "Metalloid"]
        else:
            if value1 == 0:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[7]] == "Solid"]
            if value1 == 1:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[7]] == "Liquid"]
            if value1 == 2:
                self.range_list = [i for i in Periodic_table.periodic_table if i[Periodic_table.range_details[7]] == "Gas"]

        self.click = "yes"
        ## calling displaying functions
        self.display_properties(5, self.propframe)
        self.display_prop1(6, self.range_list)

    def display_properties(self,row, dis_root):
        """Name of all Properties and having 2 arguments to get row number  and root from referred called function"""


        ## creating labels for dispalying property names
        self.prop1 = Label(dis_root, text=f"{Periodic_table.detail[0]}").grid(row=f"{row}", column="0", padx=5, pady=5)
        self.prop2 = Label(dis_root, text=f"{Periodic_table.detail[1]}").grid(row=f"{row}", column="1", padx=5, pady=5)
        self.prop3 = Label(dis_root, text=f"{Periodic_table.detail[2]}").grid(row=f"{row}", column="2", padx=5, pady=5)
        self.prop4 = Label(dis_root, text=f"{Periodic_table.detail[3]}").grid(row=f"{row}", column="3", padx=5, pady=5)
        self.prop5 = Label(dis_root, text=f"{Periodic_table.detail[4]}").grid(row=f"{row}", column="4", padx=5, pady=5)
        self.prop6 = Label(dis_root, text=f"{Periodic_table.detail[5]}").grid(row=f"{row}", column="5", padx=5, pady=5)
        self.prop7 = Label(dis_root, text=f'{Periodic_table.detail[6]}').grid(row=f"{row}", column="6", padx=5, pady=5)
        self.prop8 = Label(dis_root, text=f'{Periodic_table.detail[7]}').grid(row=f"{row}", column="7", padx=5, pady=5)
        self.prop9 = Label(dis_root, text=f'{Periodic_table.detail[8]}').grid(row=f"{row}", column="8", padx=5, pady=5)
        self.prop10 = Label(dis_root, text=f'{Periodic_table.detail[9]})').grid(row=f"{row}", column="9", padx=5, pady=5)
        self.prop11 = Label(dis_root, text=f'{Periodic_table.detail[10]}').grid(row=f"{row}", column="10", padx=2, pady=5)

    def content_diplay(self,root,row_no,selected,list_num):
        """displaying Elements and all of its properties"""

        self.elem_name = Label(root, text=f"{selected[list_num][0]}").grid(row=f"{row_no}", column="0", padx=1, pady=1)
        self.elem_symbo = Label(root, text=f"{selected[list_num][1]}").grid(row=f"{row_no}", column="1", padx=1, pady=1)
        self.elem_period = Label(root, text=f"{selected[list_num][2]}").grid(row=f"{row_no}", column="2", padx=1, pady=1)
        self.elem_grp = Label(root, text=f"{selected[list_num][3]}").grid(row=f"{row_no}", column="3", padx=1, pady=1)
        self.elem_atm_no = Label(root, text=f"{selected[list_num][4]}").grid(row=f"{row_no}", column="4", padx=1, pady=1)
        self.elem_mass = Label(root, text=f"{selected[list_num][5]}").grid(row=f"{row_no}", column="5", padx=1, pady=1)
        self.elem_type = Label(root, text=f"{selected[list_num][6]}").grid(row=f"{row_no}", column="6", padx=1, pady=1)
        self.elem_Electro_Nega = Label(root, text=f"{selected[list_num][7]}").grid(row=f"{row_no}", column="7", padx=1, pady=1)
        self.elem_ioniz = Label(root, text=f"{selected[list_num][8]}").grid(row=f"{row_no}", column="8", padx=1, pady=1)
        self.elem_EA = Label(root, text=f"{selected[list_num][9]}").grid(row=f"{row_no}", column="9", padx=1, pady=1)
        self.elem_state = Label(root, text=f"{selected[list_num][10]}").grid(row=f"{row_no}", column="10", padx=1, pady=1)

    def display_prop1(self,row_num, select_items):
        """Displaying property in main window if length of selected item list is less than 11"""

        item = [atm[4] for atm in select_items]
        ## button display if buttons for range of elements call the display_prop1 function
        if self.click == "yes":
            self.click_button = Button(self.propframe, text="Click to view images", command=lambda: self.img_range(item)).grid(row="4",column="5",padx=5,pady=5)
        for i in range(0, len(select_items)):
            if i < 25:
                self.content_diplay(self.propframe,row_num,select_items,i)
                row_num += 1
            else:
                self.window_popUp = Button(self.propframe, text=f"Click to view\nremaining element",command=lambda: self.remaining_pop_up(select_items,25)).grid(row="4", column="4", padx=5,pady=5)  ## button to view remaing elements

    def remaining_root(self):
        """Creating Window for remaining elements """
        self.new_window = Toplevel()  ##### creating window for remaing elements
        self.new_window.configure(bg='sky blue')
        self.propframe2 = Frame(self.new_window, bd=2, relief=SUNKEN, bg='sky blue') #pack in reamining pop up function.
        self.propframe3 = Frame(self.new_window, bd=2, relief=SUNKEN, bg='sky blue')    #pack in NExt function
        self.propframe4 = Frame(self.new_window, bd=2, relief=SUNKEN, bg='sky blue')    #pack in Next function

    def remaining_pop_up(self, select_items, limit):
        """Displaying property in new window for remaining elemnts of selected item list """
        self.remaining_root()
        self.propframe2.pack()
        self.display_properties(1, self.propframe2)
        row_num = 3
        for i in range(limit, len(select_items)):
            if i < 50:
                self.content_diplay(self.propframe2, row_num, select_items, i)
                row_num += 1
        if len(select_items) > 50:
            self.Next_button = Button(self.propframe2, text="NEXT", command=lambda: self.Next_ele(select_items))
            self.Next_button.grid(row="0", column="5")

    def Next_ele(self, select_items):
        """Displaying remaining element of list on click of next button"""
        self.propframe2.pack_forget()
        self.propframe3.pack()
        self.display_properties(1, self.propframe3)
        row_num = 3
        for i in range(50, len(select_items)):
            if i < 79:
                self.content_diplay(self.propframe3, row_num, select_items, i)
                row_num += 1
        self.Next_button.pack_forget()
        if len(select_items) > 79:
            self.propframe3.pack_forget()
            self.propframe4.pack()
            self.display_properties(1, self.propframe4)
            row_num = 3
            for i in range(79, len(select_items)):
                self.content_diplay(self.propframe4, row_num, select_items, i)
                row_num += 1

    def imageDisplay(self,img_name):
        """Displaying image for name, symbol and atomic number"""


        ## frame for image in property root ###
        self.img_frame = Frame(self.prop_root, bd=2, relief=SUNKEN, bg='sky blue')
        self.img_frame.pack()
        self.prop_root.resizable(0,0)
        self.img=[]
        row=10
        col=0
        ## Opening images using Image module of Pillow from folder where image exist
        for i in range(len(Periodic_table.img_folders)):
            try:
                self.ele_img = Image.open(f'{Periodic_table.img_folders[i]}/{img_name + 1}.png')
            except:
                self.ele_img = Image.open(f'{Periodic_table.img_folders[i]}/{img_name + 1}.jpg')

            self.ele_img = self.ele_img.resize((300, 300))  ### resizing of open images
            self.ele_img = ImageTk.PhotoImage(self.ele_img)
            self.img.append(self.ele_img)##showing image to python
        a=0
        for img in self.img:
            self.ele_img_label = Label(self.img_frame, text=f"{Periodic_table.img_folders[a].upper()}", font=("Times New Roman", 15), bg="pink").grid(row=f"{row}", column=f"{col}", columnspan="4")  # labels for text and image1
            self.ele_img_label = Label(self.img_frame, image=img).grid(row=f"{row+1}", column=f"{col}", columnspan="4")
            col+=4
            a+=1

    def Image_play(self,img_no):
        """displaying next element images on clicking forward and previous button"""

        row = 10
        col = 0
        for j in range(len(self.all_img)):
            self.ele_img_label = Label(self.img_frame2, image=self.all_img[j][img_no])
            self.ele_img_label.grid(row=f"{row + 1}", column=f"{col}", columnspan="4")
            col += 4
        self.back_button = Button(self.img_frame2, text="Previous", command=lambda: self.Previous(img_no - 1), bg="orange").grid(row="14", column="0")  ## button to get previous images
        self.frwd_button = Button(self.img_frame2, text="Next", command=lambda: self.forward(img_no + 1), bg="orange").grid(row="14",column="14")  ## button to get next images
    def img_range(self,item):
        """displaying images for range of elements in new window forward and reverse buttons"""


        ## root for displaying images of ranges of elements
        self.image_root = Toplevel()
        self.image_root.configure(bg="sky blue")
        self.image_root.geometry("1250x500+30+30")
        self.image_root.resizable(0, 0)
        self.img_frame2 = Frame(self.image_root, bd=2, relief=SUNKEN, bg='sky blue')  ###frame for presentable display of image
        self.img_frame2.pack()
        ele = []  ## getting list of images of selected items of period/group /or ranges elements
        pure = []
        use = []
        phy = []
        self.all_img=[ele,pure,use,phy]
        for img_list in range(len(self.all_img)):
            for img_name in item:
                try:
                    self.ele_img = Image.open(f'{Periodic_table.img_folders[img_list]}/{img_name}.png')

                except:
                    self.ele_img = Image.open(f'{Periodic_table.img_folders[img_list]}/{img_name}.jpg')

                self.ele_img = self.ele_img.resize((300, 300))  ### resizing of open images
                self.ele_img = ImageTk.PhotoImage(self.ele_img)  ##showing image to python
                self.all_img[img_list].append(self.ele_img)

        row = 10
        col = 0
        for j in range(len(self.all_img)):
            self.ele_label = Label(self.img_frame2, text=f"{Periodic_table.img_folders[j].upper()}",font=("Times New Roman", 15), bg="pink").grid(row=f"{row}", column=f"{col}",columnspan="4")  # labels for text and image1
            self.ele_img_label = Label(self.img_frame2, image=self.all_img[j][0])
            self.ele_img_label.grid(row=f"{row + 1}", column=f"{col}", columnspan="4")
            col += 4

        self.back_button = Button(self.img_frame2, text="Previous", command=lambda: self.Previous(0), bg="orange").grid(row="14",column="0")  ## button to get previous images
        self.frwd_button = Button(self.img_frame2, text="Next", command=lambda: self.forward(1), bg="orange").grid(row="14",column="14")  ## button to get next images

    def forward(self,img_no):
        """Displaying next images of selected item"""
        self.Image_play(img_no)
        if img_no == (len(self.all_img[0]) - 1):
            self.frwd_button = Button(self.img_frame2, text="Next", state=DISABLED).grid(row="14",column="14")  ## disabling state of button to if last image is displyed

    def Previous(self,img_no):
        """Displaying previous images of selected item"""
        self.Image_play(img_no)
        if img_no == 0:
            self.back_button = Button(self.img_frame2, text="Previous", state=DISABLED).grid(row="14",column="0")  ## disabling state of button to if last image is displyed


## creating logo window
logo=Tk()
logo.title("CODE ATOM")
logo.overrideredirect(1)   ## disabling closing nd maximizing and minimizing buttons
logo.geometry("700x500+100+100") ##### setting geometry with offsets from x and y axis
logo_img=Image.open(f"Code_Atom.png") ### opening image
logo_img=logo_img.resize((700,500))      ### resizing the image
logo_img=ImageTk.PhotoImage(logo_img) ###showing image to python
logo_label=Label(logo,image=logo_img).pack() ### packing in it

### start and exit buttons for the program
start=Button(logo_label,text="START",bg="yellow",font=("Times New Roman",10),command=Periodic_table).place(x="300",y="400")
end=Button(logo_label,text="EXIT",bg="red",font=("Times New Roman",10),command=logo.quit).place(x="375",y="400")
logo.mainloop()