import tkinter as tk
from src.die_roll_view import create_die_roll
from src.game_board_view import create_game_board
from src.models.Color import Color
from src.models.Player import Player
from src.models.Turn import Turn
from tkinter.font import Font

from src.entry_view import create_entry_view

'''
The code related to organizing canvases within frames and adding scroll bars is from 
user3300676user3300676 15722 gold badges22 silver badges77 bronze badges, et al. “Tkinter Canvas Scrollbar with Grid?” 
Stack Overflow, 1 Nov. 1966, stackoverflow.com/a/49681192/4882806.
'''

ROWS, COLS = 25, 25  # size of grid
ROWS_DISP = 15  # number of rows to display
COLS_DISP = 20  # number of columns to display


class TrivialPurfuit(tk.Tk):
    def __init__(self, title, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        helvetica_20 = Font(family='Helvetica', size=20, weight='bold')

        self.title(title)

        '''
        Create the main frame from the program that encapsulates the main view
        '''
        main_frame = tk.Frame(self, bg=Color.LIGHT_GREEN.description, bd=3, relief=tk.RIDGE)
        main_frame.grid(sticky=tk.NSEW)
        main_frame.columnconfigure(0, weight=1)

        '''
        Create a frame from name entry section of the main view
        '''
        # create a frame for name entry
        frame_entry = tk.Frame(main_frame)
        frame_entry.grid(row=3, column=0, sticky=tk.NW)

        # add canvas to this name entry frame
        canvas_entry = tk.Canvas(frame_entry, bg=Color.LIGHT_GREEN.description, borderwidth=0, highlightthickness=0)
        canvas_entry.grid(row=0, column=0)

        entry_frame = tk.Frame(canvas_entry, bg=Color.LIGHT_GREEN.description, bd=1)

        # Get player names and store them in variables
        player1 = tk.StringVar()
        player2 = tk.StringVar()
        player3 = tk.StringVar()
        player4 = tk.StringVar()

        player1_name = tk.Entry(entry_frame, textvariable=player1, bd=5)
        player1_name.grid(row=1, column=1, columnspan=8, sticky='w')
        player2_name = tk.Entry(entry_frame, textvariable=player2, bd=5)
        player2_name.grid(row=2, column=1, columnspan=8, sticky='w')
        player3_name = tk.Entry(entry_frame, textvariable=player3, bd=5)
        player3_name.grid(row=3, column=1, columnspan=8, sticky='w')
        player4_name = tk.Entry(entry_frame, textvariable=player4, bd=5)
        player4_name.grid(row=4, column=1, columnspan=8, sticky='w')

        # instantiate players, turn and player objects
        turn = Turn()
        p1 = Player('player1')
        print(p1.slices.get_slices_won())
        p1.slices.red = True
        p1.slices.white = True
        print(p1.slices.get_slices_won())
        p2 = Player('player2')
        p3 = Player('player3')
        p4 = Player('player4')

        names = {
            1: player1,
            2: player2,
            3: player3,
            4: player4
        }

        players = {
            1: p1,
            2: p2,
            3: p3,
            4: p4
        }

        create_entry_view(
            tk=tk,
            entry_frame=entry_frame,
            color=Color,
        )

        canvas_entry.create_window((0, 0), window=entry_frame, anchor=tk.NW)
        entry_frame.update_idletasks()

        '''
        Create frame for the die roll section of the main view
        '''
        # create frame for die roll
        frame_die_roll = tk.Frame(main_frame)
        frame_die_roll.grid(row=10, column=1, sticky=tk.NW)  # used to be row=4

        # add canvas to this frame
        canvas_die_roll = tk.Canvas(frame_die_roll, bg=Color.LIGHT_GREEN.description, borderwidth=0,
                                    highlightthickness=0)
        canvas_die_roll.grid(row=0, column=0)

        die_roll_frame = tk.Frame(canvas_die_roll, bg=Color.LIGHT_GREEN.description, bd=1)

        create_die_roll(
            tk=tk,
            frame=die_roll_frame,
            color=Color
        )

        canvas_die_roll.create_window((0, 0), window=die_roll_frame, anchor=tk.NW)
        die_roll_frame.update_idletasks()

        # create frame for board game and scroll bar
        frame_board_game = tk.Frame(main_frame)
        frame_board_game.grid(row=10, column=0, sticky=tk.NW)

        # add canvas to the frame
        canvas_board_game = tk.Canvas(frame_board_game, bg=Color.WHITE.description)
        canvas_board_game.grid(row=10, column=0)

        # create vertical scroll bar
        vsbar = tk.Scrollbar(frame_board_game, orient=tk.VERTICAL, command=canvas_board_game.yview)
        vsbar.grid(row=10, column=1, sticky=tk.NS)
        canvas_board_game.configure(yscrollcommand=vsbar.set)

        # create horizontal scroll bar
        hsbar = tk.Scrollbar(frame_board_game, orient=tk.HORIZONTAL, command=canvas_board_game.xview)
        hsbar.grid(row=1, column=0, sticky=tk.EW)
        canvas_board_game.configure(xscrollcommand=hsbar.set)

        # create a frame for the board game
        buttons_frame = tk.Frame(canvas_board_game, bg=Color.LIGHT_BLUE.description, bd=1)

        create_game_board(
            tk_button=tk.Button,
            root_window=buttons_frame,
            font_type=helvetica_20,
            start_row=0,
            sq_dim=7,
            color_enum=Color,
            names_dict=names,
            players_dict=players,
            turn=turn
        )

        canvas_board_game.create_window((0, 0), window=buttons_frame, anchor=tk.NW)

        buttons_frame.update_idletasks()
        bbox = canvas_board_game.bbox(tk.ALL)

        # define the scrollable region
        w, h = bbox[2] - bbox[1], bbox[3] - bbox[1]
        dw, dh = int((w / COLS) * COLS_DISP), int((h / ROWS) * ROWS_DISP)
        canvas_board_game.configure(scrollregion=bbox, width=dw, height=dh)


if __name__ == "__main__":
    app = TrivialPurfuit("Trivial Purfuit by Software Titans")
    app.mainloop()
