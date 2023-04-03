########################################################
#---------------- github.com/duruburak ----------------#
########################################################

import random
from tkinter.messagebox import showinfo

import customtkinter as ctk
from PIL import Image


class TickTackToe(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.player_x = ctk.CTkImage(light_image=Image.open("icons/icon_x.png"),
                                    dark_image=Image.open("icons/icon_x.png"),
                                    size=(40, 40))
        self.player_o = ctk.CTkImage(light_image=Image.open("icons/icon_o.png"),
                                    dark_image=Image.open("icons/icon_o.png"),
                                    size=(50, 50))
        
        self.chosen_side = self.player_x
        self.ai_side = self.player_o
        self.chosen_mark = "X"
        self.ai_mark = "O"
        self.whose_move_var = ctk.StringVar(value="X")

        self.round: int

        self.minsize(700, 670)
        self.title("Tic Tac Toe")

        self.choose_container = ctk.CTkFrame(self, fg_color="gray14", bg_color="gray14")
        self.choose_x = ctk.CTkButton(self.choose_container, state="normal", width=45, height=40, corner_radius=12, text="X", text_color="red", text_color_disabled="red", font=("Arial", 30, "bold"), fg_color="gray14", bg_color="gray14", hover_color="gray17", command=self.x_is_chosen_side)
        self.choose_o = ctk.CTkButton(self.choose_container, state="normal", width=45, height=40, corner_radius=12, text="O", text_color="blue", text_color_disabled="blue", font=("Arial", 30, "bold"), fg_color="gray14", bg_color="gray14", hover_color="gray17", command=self.o_is_chosen_side)
        self.start_button = ctk.CTkButton(self, text="START", width=20, height=15, corner_radius=30, font=("Batang", 20, "bold"), fg_color="gray17", bg_color="gray14", hover_color="purple", command=self.start_game)
        self.main_frame = ctk.CTkFrame(self)

        self._cells = {}
        self._textvariables = {}
        self._cell_buttons = {}
        for i in range(1,10):
            self._cells[i] = ctk.CTkFrame(self.main_frame, fg_color="gray14", bg_color="gray14")
            self._textvariables[i] = ctk.IntVar(value=i)
            self._cell_buttons[i] = ctk.CTkButton(self._cells[i], text="", state="disabled", height=150, width=150, fg_color="#543864", bg_color="gray14", hover_color="#54123B", textvariable= self._textvariables[i], command=lambda j=i: self.player_move(j))
        
        self._occupied_cells: dict
        self._available_cells: dict

        self._create_board()
        self.iconbitmap("icons/iconbitmap.ico")


    def _create_board(self):

        self.choose_container.pack(pady=(5,0), padx=10)
        self.choose_x.pack(side="left", pady=10, padx=20)
        self.choose_o.pack(side="left", pady=10, padx=20)
        self.start_button.pack(pady=(5,10), ipadx=1, ipady=5)
        self.main_frame.pack(pady=(10,1), padx=10)

        self.main_frame.columnconfigure((0,2), weight=1)
        self.main_frame.rowconfigure((0,2), weight=1)

        self._cells[1].grid(row=0, column=0, pady=5, padx=5, sticky="se")
        self._cells[2].grid(row=0, column=1, pady=5, padx=5, sticky="swe")
        self._cells[3].grid(row=0, column=2, pady=5, padx=5, sticky="sw")
        self._cells[4].grid(row=1, column=0, pady=5, padx=5, sticky="nse")
        self._cells[5].grid(row=1, column=1, pady=5, padx=5, sticky="nswe")
        self._cells[6].grid(row=1, column=2, pady=5, padx=5, sticky="nsw")
        self._cells[7].grid(row=2, column=0, pady=5, padx=5, sticky="ne")
        self._cells[8].grid(row=2, column=1, pady=5, padx=5, sticky="nwe")
        self._cells[9].grid(row=2, column=2, pady=5, padx=5, sticky="nw")

        for i in range(1,10):
            self._cell_buttons[i].configure(image=None)
            self._cell_buttons[i].pack(fill="both", expand=True)

        self._occupied_cells = {1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}
        self._available_cells = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8:9}


    def start_game(self):

        self.choose_x.configure(state="disabled")
        self.choose_o.configure(state="disabled")
        
        self.round = 1
        self._create_board()
        
        for k in self._cell_buttons.values():
            k.configure(state="normal")

        self.play()


    def x_is_chosen_side(self):

        self.chosen_side = self.player_x
        self.ai_side = self.player_o
        self.chosen_mark = "X"
        self.ai_mark = "O"
        self.whose_move_var.set("X")


    def o_is_chosen_side(self):

        self.chosen_side = self.player_o
        self.ai_side = self.player_x
        self.chosen_mark = "O"
        self.ai_mark = "X"
        self.whose_move_var.set("O")


    def player_move(self, index):
        
        self._cell_buttons[index].configure(image=self.chosen_side, state="disabled")
        del self._available_cells[index-1]
        self._occupied_cells[index] = self.chosen_mark

        self.whose_move_var.set(self.ai_mark)
    

    def ai_move(self):

        chosen_value_ai = random.choice(list(self._available_cells.values()))

        if (self._occupied_cells[1] is self._occupied_cells[5] is self.chosen_mark) or (self._occupied_cells[5] is self._occupied_cells[9] is self.chosen_mark) or (self._occupied_cells[1] is self._occupied_cells[9] is self.chosen_mark):
            
            if (self._occupied_cells[1] == "-") and (1 in list(self._available_cells.values())):
                chosen_value_ai = 1
            elif (self._occupied_cells[9] == "-") and (9 in list(self._available_cells.values())):
                chosen_value_ai = 9
            elif (self._occupied_cells[5] == "-") and (5 in list(self._available_cells.values())):
                chosen_value_ai = 5
        elif (self._occupied_cells[3] is self._occupied_cells[5] is self.chosen_mark) or (self._occupied_cells[5] is self._occupied_cells[7] is self.chosen_mark) or (self._occupied_cells[3] is self._occupied_cells[7] is self.chosen_mark):
            
            if (self._occupied_cells[3] == "-") and (3 in list(self._available_cells.values())):
                chosen_value_ai = 3
            elif (self._occupied_cells[7] == "-") and (7 in list(self._available_cells.values())):
                chosen_value_ai = 7
            elif (self._occupied_cells[5] == "-") and (5 in list(self._available_cells.values())):
                chosen_value_ai = 5
        else:

            for i in [1, 4, 7]:
                if (self._occupied_cells[i] is self._occupied_cells[i+1] is self.chosen_mark) or (self._occupied_cells[i] is self._occupied_cells[i+2] is self.chosen_mark):
                    if (self._occupied_cells[i+2] == "-") and (i+2 in list(self._available_cells.values())):
                        chosen_value_ai = i+2
                    elif (self._occupied_cells[i+1] == "-") and (i+1 in list(self._available_cells.values())):
                        chosen_value_ai = i+1
        
            for i in [1, 2, 3]:
                if (self._occupied_cells[i] is self._occupied_cells[i+3] is self.chosen_mark) or (self._occupied_cells[i] is self._occupied_cells[i+6] is self.chosen_mark):
                    if (self._occupied_cells[i+3] == "-") and (i+3 in list(self._available_cells.values())):
                        chosen_value_ai = i+3
                    elif (self._occupied_cells[i+6] == "-") and (i+6 in list(self._available_cells.values())):
                        chosen_value_ai = i+6


        final_chosen_value = chosen_value_ai

        self._cell_buttons[final_chosen_value].configure(image=self.ai_side, state="disabled")
        del self._available_cells[final_chosen_value-1]     
        self._occupied_cells[final_chosen_value] = self.ai_mark   
        
        self.whose_move_var.set(self.chosen_mark)


    def play(self):

        if self.chosen_mark == "X":
            while True:
                self.wait_variable(self.whose_move_var)
                
                if self.round > 1:
                    if self.check_if_win():
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return
                    if self.round > 4 and self.check_if_win() == False:
                        showinfo(title=f"Game Over! It's a draw.", message="The game resulted in a draw.")
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return
                    
                self.ai_move()

                if self.round > 1:
                    if self.check_if_win():
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return
                    if self.round > 4 and self.check_if_win() == False:
                        showinfo(title=f"Game Over! It's a draw.", message="The game resulted in a draw.")
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return

                self.round += 1

        elif self.chosen_mark == "O":
            while True:
                self.ai_move()

                if self.round > 1:
                    if self.check_if_win():
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return
                    if self.round > 4 and self.check_if_win() == False:
                        showinfo(title=f"Game Over! It's a draw.", message="The game resulted in a draw.")
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return

                self.wait_variable(self.whose_move_var)

                if self.round > 1:
                    if self.check_if_win():
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return
                    if self.round > 4 and self.check_if_win() == False:
                        showinfo(title=f"Game Over! It's a draw.", message="The game resulted in a draw.")
                        self.choose_x.configure(state="normal")
                        self.choose_o.configure(state="normal")
                        return

                self.round += 1
                

    def check_if_win(self):

        if (self._occupied_cells[1] is self._occupied_cells[2] is self._occupied_cells[3]) and (self._occupied_cells[3] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[3]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")

            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[4] is self._occupied_cells[5] is self._occupied_cells[6]) and (self._occupied_cells[6] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[6]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[7] is self._occupied_cells[8] is self._occupied_cells[9]) and (self._occupied_cells[9] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[9]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[1] is self._occupied_cells[4] is self._occupied_cells[7]) and (self._occupied_cells[7] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[7]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[2] is self._occupied_cells[5] is self._occupied_cells[8]) and (self._occupied_cells[8] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[8]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[3] is self._occupied_cells[6] is self._occupied_cells[9]) and (self._occupied_cells[9] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[9]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[1] is self._occupied_cells[5] is self._occupied_cells[9]) and (self._occupied_cells[9] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[9]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True

        elif (self._occupied_cells[3] is self._occupied_cells[5] is self._occupied_cells[7]) and (self._occupied_cells[7] in [self.chosen_mark, self.ai_mark]):
            winner_mark = self._occupied_cells[7]
            winner = "The Player" if winner_mark == self.chosen_mark else "The Computer"
            showinfo(title=f"Game Over! {winner} has won!", message=f"The game resulted in {winner}'s win.")
            
            for k in self._cell_buttons.values():
                k.configure(state="disabled")

            return True
        else:
            return False


def main():
    board = TickTackToe()
    board.mainloop()

if __name__ == "__main__":
    main()