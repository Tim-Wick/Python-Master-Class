import sqlite3
import tkinter

# conn = sqlite3.connect("music.sqlite")


class Scrollbox(tkinter.Listbox):

    def __init__(self, box, **kwargs):
        super().__init__(box, **kwargs)

        self.scrollbar = tkinter.Scrollbar(box, orient=tkinter.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, stick="nse", rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):

    def __init__(self, box, connection, table, field, sort_order=(), **kwargs):
        super().__init__(box, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.link_value = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind("<<ListboxSelect>>", self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        self.link_value = link_value  # store the id, so we know the "master" records we're populated from
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + "=?" + self.sql_sort
            self.cursor.execute(sql, (link_value,))
        else:
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear listbox contents before reoloading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            index = self.curselection()[0]
            value = self.get(index),

            # Get the ID from the database row and make sure we get correct one by incl. link_value
            if self.link_value:
                value = value[0], self.link_value
                sql_where = " WHERE " + self.field + "=? AND " + self.link_field + "=?"
            else:
                sql_where = " WHERE " + self.field + "=?"

            link_id = self.cursor.execute(self.sql_select + sql_where, value).fetchone()[1]
            self.linked_box.requery(link_id)


# def get_songs(event):
#     lb = event.widget
#     index = int(lb.curselection()[0])
#     album_name = lb.get(index),
#
#     # get the artist ID from DB row
#     album_id = conn.execute("SELECT albums._id FROM albums WHERE albums.name = ?", album_name).fetchone()
#     alist = []
#     for x in conn.execute("SELECT songs.title FROM songs WHERE songs.album = ? ORDER BY songs.track", album_id):
#         alist.append(x[0])
#     song_lv.set(tuple(alist))


if __name__ == "__main__":
    conn = sqlite3.connect("music.sqlite")
    window = tkinter.Tk()
    window.title("Music DB Browser")
    window.geometry("1024x768")

    window.columnconfigure(0, weight=2)
    window.columnconfigure(1, weight=2)
    window.columnconfigure(2, weight=2)
    window.columnconfigure(3, weight=1)  # spacer columns on right

    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=5)
    window.rowconfigure(2, weight=5)
    window.rowconfigure(3, weight=1)

    # labels
    tkinter.Label(window, text="Artists").grid(row=0, column=0)
    tkinter.Label(window, text="Albums").grid(row=0, column=1)
    tkinter.Label(window, text="Songs").grid(row=0, column=2)

    # Artists listbox
    artist_list = DataListBox(window, conn, "artists", "name")
    artist_list.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
    artist_list.config(border=2, relief="sunken")

    artist_list.requery()

    # Albums listbox
    album_lv = tkinter.Variable(window)
    album_lv.set(("Choose an artist",))
    album_list = DataListBox(window, conn, "albums", "name", sort_order=("name",))
    album_list.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
    album_list.config(border=2, relief="sunken")

    # album_list.bind("<<ListboxSelect>>", get_songs)
    artist_list.link(album_list, "artist")

    # Songs listbox
    song_lv = tkinter.Variable(window)
    song_lv.set(("Choose an Album",))
    song_list = DataListBox(window, conn, "songs", "title", ("track", "title"))
    song_list.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
    song_list.config(border=2, relief="sunken")

    album_list.link(song_list, "album")

    # Main loop
    window.mainloop()
    print("Closing DB connection")
    conn.close()
