import streamlit as st
import streamlit_menu as menu


header = {'logo': 'base64-image-string', 'title': 'Gmail Clone'}

menu_items = [
    {
        "id": 1,
        "title": "Social",
        "icon": "fa-solid fa-users",
        "children": None,
    },
    {
        "id": 2,
        "title": "Starred",
        "icon": "fa-solid fa-star",
        "children": None,
    },
    {
        "id": 3,
        "title": "All mails",
        "icon": "fa-solid fa-envelope",
        "children": [
            {
                "id": 4,
                "title": "Sent",
                "icon": "fa-solid fa-share-from-square",
                "children": None,
            },
            {
                "id": 5,
                "title": "Important",
                "icon": "fa-solid fa-tag",
                "children": None,
            },
            {
                "id": 6,
                "title": "Spam",
                "icon": "fa-solid fa-triangle-exclamation",
                "children": None,
            },
        ],
    },
    {
        "id": 7,
        "title": "Bin",
        "icon": "fa-solid fa-trash-can",
        "children": None,
    },
    {
        "id": 8,
        "title": "Settings",
        "icon": "fa-solid fa-gear",
        "children": None,
    },
    {
        "id": 9,
        "title": "Logout",
        "icon": "fa-solid fa-right-from-bracket",
        "children": None,
    },
]


def on_menu_select(widgetkey):

    # Prints the selected menu item on the console

    print(st.session_state["sidemenu"]["title"])


menu.st_menu(
    header=header,
    menu_items=menu_items,
    on_menu_select=on_menu_select,
    args=("sidemenu",),
)
