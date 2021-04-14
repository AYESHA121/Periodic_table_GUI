from tkinter import *
from PIL import Image ,ImageTk


## All properties periodic table have
detail=["Name of Element","Symbol of Element","Period Number ","Group Number","Atomic Number","Mass number","Type","Electronegativity\n(KJ/mol)","Ionization energy\n(KJ/mol)","Electron affinity\n(KJ/mol)","State"]
range_details = {1:4,2:5,3:7,4:8,5:9,6:6,7:10}

def Start_root():
    """Main window opens after starting"""
    global window
    global topframe
    global centerframe
    global root
    ### Creating tkinter window
    window=Toplevel()
    window.title("CODE ATOM")
    window.configure(bg='sky blue') ## background colour of window
    window.resizable(0,0)
    window.minsize(350, 500) ### defining minimum size of window width=350,height=500

    ## Creating frame for putting all labels and buttons in representable style
    topframe = Frame(window, bd=2, relief=SUNKEN, bg='sky blue')
    topframe.pack()
    centerframe = Frame(window, bd=2, relief=SUNKEN, bg='sky blue')
    centerframe.pack()
    root = Frame(window, bd=2, relief=SUNKEN)
    root.pack()

    ### main label and buttons for main window
    mode = Label(topframe, text="Information of elements in periodic table", font=("Times New Roman", 15), border=5,relief="raised")
    mode.grid(row="0", column="0", columnspan="10", padx=10, pady=10)
    single = Button(topframe, text="To quer single \nelement/period/group", anchor=W, command=properties_single)
    single.grid(row="2", column="0", pady=10, padx=5)
    range_elem = Button(topframe, text="To quer a range \nof elements", anchor=E, command=range_properties)
    range_elem.grid(row="2", column="9", pady=5, padx=5)


def make_periodic_table():
    """importing data from text file and making list of all list elements"""
    Table = open("Periodic_Table.txt","r")
    periodic_table = []
    for element in Table:
        element = element.rstrip()
        element = element.split(",")
        periodic_table.append(element)
    Table.close()
    return periodic_table
periodic_table = make_periodic_table()


def properties_single():
    """Buttons for single element """

    ## creating buttons and call the functions on clicking button
    name_button = Button(centerframe, text="Name of Element",command=Name_of_Element)
    name_button.grid(row="3", column="0",padx=5,pady=5)
    symbol_button = Button(centerframe, text="Symbol of Element",command=Symbol)
    symbol_button.grid(row="3", column="1",padx=5,pady=5)
    period_button = Button(centerframe, text="Period Number \nof Table(1-7)",command=Period)
    period_button.grid(row="3", column="2",padx=5,pady=5)
    group_button = Button(centerframe, text="Group Number \nof Table(1-18)",command=Group)
    group_button.grid(row="3", column="3", padx=5, pady=5)
    Atomic_no_button = Button(centerframe, text="Atomic Number \nof Element",command=Atomic_no)
    Atomic_no_button.grid(row="3", column="4",padx=5,pady=5)

def range_properties():
    """buttons for range of elements"""

    ## creating buttons and call the functions on clicking button
    atomic_button = Button(centerframe, text="Range of atomic number",command=atm_rannges)
    atomic_button.grid(row="6", column="0",padx=5,pady=5)
    mass_button = Button(centerframe, text="Range of Mass number",command=mass)
    mass_button.grid(row="6", column="1",padx=5,pady=5)
    electroneg_button = Button(centerframe, text="Range of Electronegativity\n(KJ/mol)",command=EN_ranges)
    electroneg_button.grid(row="6", column="2",padx=5,pady=5)
    ioniz_button = Button(centerframe, text="Range of Ionization energy\n(KJ/mol))",command=IE_ranges)
    ioniz_button.grid(row="6", column="3", padx=5, pady=5)
    elec_aff_button = Button(centerframe, text="Range of Electron affinity\n(KJ/mol)",command=EA_ranges)
    elec_aff_button.grid(row="6", column="4",padx=5,pady=5)
    type_button = Button(centerframe, text="Type(Metal/\nMetalloid/Non-Metal)", command=TyPe)
    type_button.grid(row="6", column="5", padx=5, pady=5)
    state_button = Button(centerframe, text="State", command=State)
    state_button.grid(row="6", column="6", padx=5, pady=5)


def display_properties(row,dis_root):
    """Name of all Properties and having 2 arguments to get row number  and root from referred called function"""
    global propframe
    global new_windowframe

    ## creating labels for dispalying property names
    prop=Label(dis_root,text=f"{detail[0]}").grid(row=f"{row}", column="0",padx=5,pady=5)
    prop=Label(dis_root,text=f"{detail[1]}").grid(row=f"{row}", column="1",padx=5,pady=5)
    prop=Label(dis_root,text=f"{detail[2]}").grid(row=f"{row}", column="2",padx=5,pady=5)
    prop=Label(dis_root,text=f"{detail[3]}").grid(row=f"{row}", column="3",padx=5,pady=5)
    prop=Label(dis_root,text=f"{detail[4]}").grid(row=f"{row}", column="4",padx=5,pady=5)
    prop=Label(dis_root,text=f"{detail[5]}").grid(row=f"{row}", column="5",padx=5,pady=5)
    prop=Label(dis_root,text=f'{detail[6]}').grid(row=f"{row}", column="6",padx=5,pady=5)
    prop=Label(dis_root,text=f'{detail[7]}').grid(row=f"{row}", column="7",padx=5,pady=5)
    prop=Label(dis_root,text=f'{detail[8]}').grid(row=f"{row}", column="8",padx=5,pady=5)
    prop=Label(dis_root,text=f'{detail[9]})').grid(row=f"{row}", column="9",padx=5,pady=5)
    prop=Label(dis_root,text=f'{detail[10]}').grid(row=f"{row}", column="10",padx=2,pady=5)



def display_prop1(row_no,select_items,click):
    global propframe
    """Displaying property in main window if length of selected item list is less than 11"""
    selected=select_items
    a = row_no
    item=[atm[4] for atm in selected]

    ## button display if buttons for range of elements call the display_prop1 function
    if click == "yes":
        click_button = Button(propframe, text="Click to view images", command=lambda: img_range(item)).grid(row="4", column="5", padx=5, pady=5)
    for i in range(0,len(selected)):
        if i<18:
            elem_name=Label(propframe,text=f"{selected[i][0]}").grid(row=f"{a}",column="0",padx=5,pady=5)
            elem_symbo=Label(propframe, text=f"{selected[i][1]}").grid(row=f"{a}",column="1",padx=5,pady=5)
            elem_period= Label(propframe, text=f"{selected[i][2]}").grid(row=f"{a}",column="2",padx=5,pady=5)
            elem_grp = Label(propframe, text=f"{selected[i][3]}").grid(row=f"{a}",column="3",padx=5,pady=5)
            elem_atm_no = Label(propframe, text=f"{selected[i][4]}").grid(row=f"{a}",column="4",padx=5,pady=5)
            elem_mass = Label(propframe, text=f"{selected[i][5]}").grid(row=f"{a}",column="5",padx=5,pady=5)
            elem_type = Label(propframe, text=f"{selected[i][6]}").grid(row=f"{a}",column="6",padx=5,pady=5)
            elem_Electro_Nega = Label(propframe, text=f"{selected[i][7]}").grid(row=f"{a}",column="7",padx=5,pady=5)
            elem_ioniz= Label(propframe, text=f"{selected[i][8]}").grid(row=f"{a}",column="8",padx=5,pady=5)
            elem_EA= Label(propframe, text=f"{selected[i][9]}").grid(row=f"{a}",column="9",padx=5,pady=5)
            elem_state = Label(propframe, text=f"{selected[i][10]}").grid(row=f"{a}",column="10",padx=5,pady=5)
            a+=1
        else:
            window_popUp=Button(propframe, text=f"Click to view\nremaining element",command=lambda: pop_up(selected)).grid(row="4",column="4",padx=5,pady=5) ## button to view remaing elements

def pop_up(select_items):
    """Displaying property in new window for remaining elemnts of selected item list """
    global propframe
    global new_windowframe
    global new_window
    selected = select_items
    new_window = Toplevel()   ##### creating window for remaing elements
    new_window.configure(bg='sky blue')
    new_windowframe=Frame(new_window,bd=2, relief=SUNKEN,bg='sky blue') # creating frame for new_window
    new_windowframe.pack()
    display_properties(1,new_windowframe)
    a=3
    for i in range(18,len(selected)):
        elem_name = Label(new_windowframe, text=f"{selected[i][0]}").grid(row=f"{a}", column="0", padx=5, pady=5)
        elem_symbo = Label(new_windowframe, text=f"{selected[i][1]}").grid(row=f"{a}", column="1", padx=5, pady=5)
        elem_period = Label(new_windowframe, text=f"{selected[i][2]}").grid(row=f"{a}", column="2", padx=5, pady=5)
        elem_grp = Label(new_windowframe, text=f"{selected[i][3]}").grid(row=f"{a}", column="3", padx=5, pady=5)
        elem_atm_no = Label(new_windowframe, text=f"{selected[i][4]}").grid(row=f"{a}", column="4", padx=5, pady=5)
        elem_mass = Label(new_windowframe, text=f"{selected[i][5]}").grid(row=f"{a}", column="5", padx=5, pady=5)
        elem_type = Label(new_windowframe, text=f"{selected[i][6]}").grid(row=f"{a}", column="6", padx=5, pady=5)
        elem_electnegativity = Label(new_windowframe, text=f"{selected[i][7]}").grid(row=f"{a}", column="7", padx=5, pady=5)
        elem_ioniz = Label(new_windowframe, text=f"{selected[i][8]}").grid(row=f"{a}", column="8", padx=5, pady=5)
        elem_elec = Label(new_windowframe, text=f"{selected[i][9]}").grid(row=f"{a}", column="9", padx=5, pady=5)
        elem_state = Label(new_windowframe, text=f"{selected[i][10]}").grid(row=f"{a}", column="10", padx=5, pady=5)
        a+= 1

def imageDisplay(img_name):
    """Displaying image for name, symbol and atomic number"""
    global ele_img
    global pure_img
    global use_img
    global phy_img

    ## frame for image in property root ###
    img_frame = Frame(prop_root, bd=2, relief=SUNKEN, bg='sky blue')
    img_frame.pack()
    ## Opening images using Image module of Pillow from folder where image exist
    try:
        ele_img=Image.open(f'presentation/{img_name+1}.png')
    except:
        ele_img =Image.open(f'presentation/{img_name+1}.jpg')

    ele_img = ele_img.resize((250, 250))   ### resizing of open images
    try:
        pure_img=Image.open(f'pure_elements/{img_name+1}.png')
    except:
        pure_img =Image.open(f'pure_elements/{img_name+1}.jpg')

    pure_img = pure_img.resize((250, 250))     ### resizing of open images
    try:
        use_img=Image.open(f'uses/{img_name+1}.png')
    except:
        use_img =Image.open(f'uses/{img_name+1}.jpg')

    use_img = use_img.resize((500, 300))      ### resizing of open images
    try:
        phy_img = Image.open(f'properties/{img_name + 1}.png')
    except:
        phy_img = Image.open(f'properties/{img_name + 1}.jpg')

    phy_img = phy_img.resize((400, 300))     ### resizing of open images

    ele_img=ImageTk.PhotoImage(ele_img)         ##showing image to python
    ele_img_label = Label(img_frame, text="Presentation",font=("Times New Roman",15),bg="pink").grid(row="10", column="0",columnspan="4")    #labels for text and image1
    ele_img_label = Label(img_frame, image=ele_img).grid(row="11",column="0",columnspan="4")


    pure_img=ImageTk.PhotoImage(pure_img)       ##showing image to python
    pure_img_label = Label(img_frame, text="Pure Form",font=("Times New Roman",15),bg="pink").grid(row="10", column="4",columnspan="4")     #labels for text and image2
    pure_img_label = Label(img_frame, image=pure_img).grid(row="11", column="4",columnspan="4")

    use_img = ImageTk.PhotoImage(use_img)       ##showing image to python
    use_img_label = Label(img_frame, text="Uses",font=("Times New Roman",15),bg="pink").grid(row="12", column="0",columnspan="4")       #labels for text and image3
    use_img_label = Label(img_frame, image=use_img).grid(row="13", column="0",columnspan="4")

    phy_img=ImageTk.PhotoImage(phy_img)     ##showing image to python
    phy_img_label=Label(img_frame, text="Properties",font=("Times New Roman",15),bg="pink").grid(row="12", column="4",columnspan="4")       #labels for text and image4
    phy_img_label = Label(img_frame, image=phy_img).grid(row="13", column="4",columnspan="4")

def img_range(item):
    """displaying images for range of elements in new window forward and reverse buttons"""
    global ele
    global pure
    global use
    global phy
    global img_frame2
    global frwd_button
    global back_button

## root for displaying images of ranges of elements
    image_root = Toplevel()
    image_root.configure(bg="sky blue")
    image_root.geometry("1000x1000+300+0")
    image_root.resizable(0,0)
    img_frame2 = Frame(image_root, bd=2, relief=SUNKEN, bg='sky blue') ###frame for presentable display of image
    img_frame2.pack()
    ele=[]              ## getting list of images of selected items of period/group /or ranges elements
    pure=[]
    use=[]
    phy=[]
    for img_name in item:
        try:
            ele_img=Image.open(f'presentation/{img_name}.png')

        except:
            ele_img =Image.open(f'presentation/{img_name}.jpg')

        ele_img = ele_img.resize((250, 250))              ### resizing of open images
        ele_img = ImageTk.PhotoImage(ele_img)             ##showing image to python
        ele.append(ele_img)
        try:
            pure_img=Image.open(f'pure_elements/{img_name}.png')
        except:
            pure_img =Image.open(f'pure_elements/{img_name}.jpg')

        pure_img = pure_img.resize((250, 250))      ### resizing of open images
        pure_img = ImageTk.PhotoImage(pure_img)     ##showing image to python
        pure.append(pure_img)

        try:
            use_img=Image.open(f'uses/{img_name}.png')

        except:
            use_img =Image.open(f'uses/{img_name}.jpg')

        use_img = use_img.resize((400, 300))        ### resizing of open images
        use_img = ImageTk.PhotoImage(use_img)       ##showing image to python
        use.append(use_img)

        try:
            phy_img=Image.open(f'properties/{img_name}.png')

        except:
            phy_img =Image.open(f'properties/{img_name}.jpg')

        phy_img = phy_img.resize((400, 300))        ### resizing of open images
        phy_img = ImageTk.PhotoImage(phy_img)       ##showing image to python
        phy.append(phy_img)

    ele_label = Label(img_frame2, text="Presentation",font=("Times New Roman",15),bg="pink").grid(row="10", column="0",columnspan="4")      #labels for text and image1
    ele_img_label = Label(img_frame2, image=ele[0])
    ele_img_label.grid(row="11",column="0",columnspan="4")

    pure_label = Label(img_frame2, text="Pure Form",font=("Times New Roman",15),bg="pink").grid(row="10", column="4",columnspan="4")        #labels for text and image2
    pure_img_label = Label(img_frame2, image=pure[0])
    pure_img_label.grid(row="11", column="4",columnspan="4")


    use_label = Label(img_frame2, text="Uses",font=("Times New Roman",15),bg="pink").grid(row="12", column="0",columnspan="4")      #labels for text and image3
    use_img_label = Label(img_frame2, image=use[0])
    use_img_label.grid(row="13", column="0",columnspan="4")
    #
    phy_label = Label(img_frame2, text="Properties", font=("Times New Roman", 15),bg="pink").grid(row="12", column="4", columnspan="4")    #labels for text and image4
    phy_img_label= Label(img_frame2, image=phy[0])
    phy_img_label.grid(row="13", column="4", columnspan="4")

    back_button = Button(img_frame2, text="Previous", command=lambda:Previous(0),bg="orange").grid(row="14", column="0")   ## button to get previous images
    frwd_button=Button(img_frame2,text="Next",command=lambda:forward(1),bg="orange").grid(row="14",column="7")              ## button to get next images

def forward(img_no):
    """Displaying next images of selected item"""
    global frwd_button
    global back_button

    ele_img_label = Label(img_frame2, image=ele[img_no])
    ele_img_label.grid(row="11", column="0", columnspan="4")

    pure_img_label = Label(img_frame2, image=pure[img_no])
    pure_img_label.grid(row="11", column="4", columnspan="4")

    use_img_label = Label(img_frame2, image=use[img_no])
    use_img_label.grid(row="13", column="0", columnspan="4")

    phy_img_label = Label(img_frame2, image=phy[img_no])
    phy_img_label.grid(row="13", column="4", columnspan="4")

    back_button = Button(img_frame2, text="Previous", command=lambda:Previous(img_no-1),bg="orange").grid(row="14", column="0")   ## button to get previous images
    frwd_button = Button(img_frame2, text="Next", command=lambda:forward(img_no+1),bg="orange").grid(row="14", column="7")    ## button to get next images
    if img_no == (len(ele) - 1):
        frwd_button = Button(img_frame2, text="Next",state=DISABLED).grid(row="14", column="7")   ## disabling state of button to if last image is displyed

def Previous(img_no):
    """Displaying previous images of selected item"""
    global frwd_button
    global back_button

    ele_img_label = Label(img_frame2, image=ele[img_no])
    ele_img_label.grid(row="11", column="0", columnspan="4")

    pure_img_label = Label(img_frame2, image=pure[img_no])
    pure_img_label.grid(row="11", column="4", columnspan="4")

    use_img_label = Label(img_frame2, image=use[img_no])
    use_img_label.grid(row="13", column="0", columnspan="4")

    phy_img_label = Label(img_frame2, image=phy[img_no])
    phy_img_label.grid(row="13", column="4", columnspan="4")

    back_button = Button(img_frame2, text="Previous", command=lambda: Previous(img_no-1),bg="orange").grid(row="14", column="0")  ## button to get previous images
    frwd_button = Button(img_frame2, text="Next", command=lambda: forward(img_no+1),bg="orange").grid(row="14", column="7")   ## button to get next images
    if img_no ==0:
        back_button = Button(img_frame2, text="Previous", state=DISABLED).grid(row="14", column="0")   ## disabling state of button to if last image is displyed

def pro_clicked(value):
    """function if any of button of single property click and displaying its output"""
    global prop_root
    global click
    global propframe
    global button
    global selected
    prop_root = Toplevel()   ## creating window for displayimg properties
    prop_root.configure(bg='sky blue')
    propframe = Frame(prop_root, bd=2, relief=SUNKEN,bg='sky blue')  ## creating frame for property root
    propframe.pack()

    if button=="single":
        click = "No"
        item_index = values.index(value)
        selected = [periodic_table[item_index]]
        imageDisplay(item_index)
    if button=="Period":
        click="yes"
        selected = [i for i in periodic_table if i[2] == str(value)]
    if button=="Group":
        click = "yes"
        selected = [i for i in periodic_table if i[3] == str(value)]
    ## calling displaying functions
    display_properties(5,propframe)
    display_prop1(6,selected,click)



def range_clicked(value1):
    """function if any of button of range properties click and displaying its output"""
    global propframe
    global click
    global prop_root
    prop_root = Toplevel()          ## creating root for displaying properties of ranges of elements
    prop_root.configure(bg='sky blue')
    propframe = Frame(prop_root, bd=2, relief=SUNKEN, bg='sky blue')      ## creating frame in property root for displaying properties of ranges of elements
    propframe.pack()
    global ranges
    global range_list
    if ranges=="Atomic_no":
        if value1==0:
            range_list=[i for i in periodic_table if 1 <= float(i[range_details[1]]) <= 30]
        elif value1==1:
            range_list=[i for i in periodic_table if 30<= float(i[range_details[1]]) <= 60 ]
        elif value1==2:
            range_list=[i for i in periodic_table if 60 <= float(i[range_details[1]]) <= 90]
        else:
            range_list=[i for i in periodic_table if 90 <= float(i[range_details[1]]) <= 118]
    elif ranges=="mass":
        if value1==0:
            range_list=[i for i in periodic_table if 1 <= float(i[range_details[2]]) <= 75]
        elif value1==1:
            range_list=[i for i in periodic_table if 75<= float(i[range_details[2]]) <= 150]
        elif value1==2:
            range_list=[i for i in periodic_table if 150 <= float(i[range_details[2]]) <= 225]
        else:
            range_list=[i for i in periodic_table if 225 <= float(i[range_details[2]]) <= 300]
    elif ranges == "Electronegativity":
        if value1==0:
            range_list=[i for i in periodic_table if i[range_details[3]] != "N/A" if 0 <= float(i[range_details[3]]) <= 1]
        elif value1==1:
            range_list=[i for i in periodic_table if i[range_details[3]] != "N/A" if 1 <= float(i[range_details[3]]) <= 2 ]
        elif value1==2:
            range_list=[i for i in periodic_table if i[range_details[3]] != "N/A" if 2 <= float(i[range_details[3]]) <= 3]
        else:
            range_list=[i for i in periodic_table if i[range_details[3]] == "N/A"]
    elif ranges=="Ionization Energy":
        if value1==0:
            range_list=[i for i in periodic_table if i[range_details[4]] != "N/A" if 300 <= float(i[range_details[4]]) <= 500]
        elif value1==1:
            range_list=[i for i in periodic_table if i[range_details[4]] != "N/A" if 500<= float(i[range_details[4]]) <= 1000 ]
        elif value1==2:
            range_list=[i for i in periodic_table if i[range_details[4]] != "N/A" if 1000 <= float(i[range_details[4]]) <= 1500]
        else:
            range_list=[i for i in periodic_table if i[range_details[4]] == "N/A"]
    elif ranges=="Electron Affinity":
        if value1==0:
            range_list=[i for i in periodic_table if i[range_details[5]] != "N/A" if 0 <= float(i[range_details[5]]) <= 100]
        elif value1==1:
            range_list=[i for i in periodic_table if i[range_details[5]] != "N/A" if 100<= float(i[range_details[5]]) <= 250 ]
        elif value1==2:
            range_list=[i for i in periodic_table if i[range_details[5]] != "N/A" if 250 <= float(i[range_details[5]]) <= 400]
        else:
            range_list=[i for i in periodic_table if i[range_details[5]] == "N/A"]
    elif ranges=="Type":
        if value1==0:
            range_list = [i for i in periodic_table if i[range_details[6]] == "Metal"]
        if value1==1:
            range_list = [i for i in periodic_table if i[range_details[6]]== "Non Metal"]
        if value1==2:
            range_list = [i for i in periodic_table if i[range_details[6]] == "Metalloid"]
    else:
        if value1==0:
            range_list = [i for i in periodic_table if i[range_details[7]] == "Solid"]
        if value1==1:
            range_list = [i for i in periodic_table if i[range_details[7]]== "Liquid"]
        if value1==2:
            range_list = [i for i in periodic_table if i[range_details[7]] == "Gas"]
    click="yes"

    ## calling displaying functions
    display_properties(rows,propframe)
    display_prop1(rows+1,range_list,click)


def Name_of_Element():
    """Creating button for name of element and call the function on click"""
    global variable1
    global button
    global values
    button = "single"
    values = [i[0] for i in periodic_table]         ## getting list of names from periodic table
    variable1=StringVar()                           ## defining variable
    variable1.set(values[0])                        ## setting default value of variable
    name=OptionMenu(centerframe,variable1,*values,command=pro_clicked)      ## button having menu  and call the function
    name.grid(row="4", column="0",padx=5,pady=5)

def Symbol():
    "Creating button for symbol of element and call the function on click"
    global variable1
    global button
    global values
    button="single"
    values = [i[1] for i in periodic_table]         ## getting list of symbol from periodic table
    variable1=StringVar()                           ## defining variable
    variable1.set(values[0])                        ## setting default value of variable
    symbol =OptionMenu(centerframe,variable1,*values,command=pro_clicked)       ## button having menu  and call the function
    symbol.grid(row="4",column="1",padx=5,pady=5)


def Period():
    """Creating button for all elements of period number selected and call the function on click"""
    global variable1
    global button
    button="Period"
    values=[1,2,3,4,5,6,7]          ## list of all period numbers
    variable1=IntVar()              ## defining variable
    variable1.set(values[0])        ## setting default value of variable
    period = OptionMenu(centerframe,variable1,*values,command=pro_clicked)          ## button having menu  and call the function
    period.grid(row="4",column="2",padx=5,pady=5)


def Group():
    """Creating button for all elements of group number selected and call the function on click"""
    global variable1
    global button
    button="Group"
    values=[i for i in range(1,19)]  ###list of all group numbers
    variable1=IntVar()                  ## defining variable
    variable1.set(values[0])            ## setting default value of variable
    period = OptionMenu(centerframe,variable1,*values,command=pro_clicked)      ## button having menu  and call the function
    period.grid(row="4",column="3",padx=5,pady=5)

def Atomic_no():
    """Creating button for atomic number of element and call the function on click"""
    global variable1
    global button
    global values
    button = "single"
    values = [i[4] for i in periodic_table]     ## getting list of atomic number from periodic table
    variable1 = StringVar()                     ## defining variable
    variable1.set(values[0])                    ## setting default value of variable
    symbol = OptionMenu(centerframe, variable1, *values, command=pro_clicked)       ## button having menu  and call the function
    symbol.grid(row="4", column="4",padx=5,pady=5)



def atm_rannges():
    """Creating button for range of atomic numbers of element and call the function on click"""
    global ranges
    global rows
    ranges = "Atomic_no"
    range_Atom = IntVar()
    options = [("1-30", 0), ("30-60", 1), ("60-90", 2),("90-118",3)]
    rows=7
    for text, r_value in options:           ## buttons having options  and call the function
        Radiobutton(centerframe, text=text, variable=range_Atom, value=r_value,command=lambda: range_clicked(range_Atom.get())).grid(row=f"{rows}", column="0", padx=5, pady=5)
        rows+=1
def mass():
    """Creating mass button for range of mass numbers of element and call the function on click"""
    global ranges
    global rows
    ranges = "mass"
    range_mass = IntVar()
    options = [("1-75", 0), ("75-150", 1), ("150-225", 2), ("225-300", 3)]
    rows=7
    for text, r_value in options:       ## buttons having options  and call the function
        Radiobutton(centerframe, text=text, variable=range_mass, value=r_value,command=lambda: range_clicked(range_mass.get())).grid(row=f"{rows}", column="1", padx=5, pady=5)
        rows+=1

def EN_ranges():
    """Creating electronegativity button for range of electronegativity of element and call the function on click"""
    global ranges
    global rows
    ranges="Electronegativity"
    range_EN=IntVar()
    options=[("0-1",0),("1-2",1),("2-3",2),("N/A",3)]
    rows=7
    for text,r_value in options:            ## buttons having options  and call the function
        Radiobutton(centerframe,text=text,variable=range_EN,value=r_value,command=lambda:range_clicked(range_EN.get())).grid(row=f"{rows}",column="2",padx=5,pady=5)
        rows+=1

def IE_ranges():
    """Creating ionization energy button for range of ionization energy of element and call the function on click"""
    global ranges
    global rows
    ranges = "Ionization Energy"
    range_IE=IntVar()
    options = [("100-500", 0), ("500-1000", 1), ("1000-1500", 2), ("N/A", 3)]
    rows=7
    for text, r_value in options:       ## buttons having options  and call the function
        Radiobutton(centerframe, text=text, variable=range_IE, value=r_value,command=lambda: range_clicked(range_IE.get())).grid(row=f"{rows}", column="3", padx=5, pady=5)
        rows+=1
def EA_ranges():
    """Creating electron affinity button for range of electron affinity of element and call the function on click"""
    global ranges
    global rows
    ranges="Electron Affinity"
    range_EA=IntVar()
    options=[("0-100",0),("100-250",1),("250-400",2),("N/A",3)]
    rows=7
    for text,r_value in options:        ## buttons having options  and call the function
        Radiobutton(centerframe,text=text,variable=range_EA,value=r_value,command=lambda:range_clicked(range_EA.get())).grid(row=f"{rows}",column="4",padx=5,pady=5)
        rows+=1
def TyPe():
    """Creating type button for elements having same type and call the function on click"""
    global ranges
    global rows
    ranges = "Type"
    range_Type = IntVar()
    options = [("Metal", 0), ("Non-Metal", 1), ("Metalloid", 2)]
    rows=7
    for text, r_value in options:           ## buttons having options  and call the function
        Radiobutton(centerframe, text=text, variable=range_Type, value=r_value,command=lambda: range_clicked(range_Type.get())).grid(row=f"{rows}", column="5", padx=5, pady=5)
        rows+=1
def State():
    """Creating state button for elements having same state and call the function on click"""
    global ranges
    global rows
    ranges = "State"
    range_State = IntVar()
    options = [("Solid", 0), ("Liquid", 1), ("Gas", 2)]
    rows=7
    for text, r_value in options:       ## buttons having options  and call the function
        Radiobutton(centerframe, text=text, variable=range_State, value=r_value,command=lambda: range_clicked(range_State.get())).grid(row=f"{rows}", column="6", padx=5, pady=5)
        rows+=1




#######   Main program ######


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
start=Button(logo_label,text="START",bg="yellow",font=("Times New Roman",10),command=Start_root).place(x="300",y="400")
end=Button(logo_label,text="EXIT",bg="red",font=("Times New Roman",10),command=logo.quit).place(x="375",y="400")

logo.mainloop()
