import random
import os
import arcade
import arcade.gui
import time

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 775
SCREEN_TITLE = "Hangman"

#Starting Screen
class Start(arcade.View):
    
    def __init__(self):
        super().__init__()

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()

        arcade.draw_circle_outline(720, 650, 10, arcade.color.WHITE)
        arcade.draw_circle_outline(720, 675, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(700, 680, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(740, 680, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(700, 680, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(740, 680, 5, arcade.color.BLACK)
        arcade.draw_line(720, 755, 720, 725, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 720, 755, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 625, 455, arcade.color.WHITE, 1)
        arcade.draw_line(580, 455, 860, 455, arcade.color.WHITE, 1)
        arcade.draw_line(720, 625, 720, 525, arcade.color.WHITE, 1)
        arcade.draw_line(720, 525, 690, 475, arcade.color.WHITE, 1)
        arcade.draw_line(720, 525, 750, 475, arcade.color.WHITE, 1)
        arcade.draw_line(720, 600, 750, 550, arcade.color.WHITE, 1)
        arcade.draw_line(720, 600, 690, 550, arcade.color.WHITE, 1)

        arcade.draw_text("Hangman", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size = 50, anchor_x = "center")
        arcade.draw_text("Press enter/return to start", self.window.width / 2, self.window.height / 2.5, arcade.color.WHITE, font_size = 20, anchor_x = "center")

    def on_key_press(self, symbol, modifiers):
        """Handles user input
        Letter Keys: Whatever key was pressed was entered as guess
        ESC: Quit the game"""

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.ENTER:
            play_screen = PlayScreen()
            play_screen.setup()
            self.window.show_view(play_screen)

#Screen where game is played
class PlayScreen(arcade.View):

    def __init__(self, initial_score = 0, all_time = 0):
        super().__init__()
        self.score = initial_score
        self.high_score = all_time

        #UI Manager to handle UI
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        #Create 3 horizontal layouts
        self.h_box1 = arcade.gui.UIBoxLayout(720, 500, False)
        self.h_box2 = arcade.gui.UIBoxLayout(720, 400, False)
        self.h_box3 = arcade.gui.UIBoxLayout(720, 300, False)

        #Create vertical layout to hold other layouts
        self.v_box = arcade.gui.UIBoxLayout()

        #Create buttons
        self.a = arcade.gui.UIFlatButton(text = "A", width = 75)
        self.b = arcade.gui.UIFlatButton(text = "B", width = 75)
        self.c = arcade.gui.UIFlatButton(text = "C", width = 75)
        self.d = arcade.gui.UIFlatButton(text = "D", width = 75)
        self.e = arcade.gui.UIFlatButton(text = "E", width = 75)
        self.f = arcade.gui.UIFlatButton(text = "F", width = 75)
        self.g = arcade.gui.UIFlatButton(text = "G", width = 75)
        self.h = arcade.gui.UIFlatButton(text = "H", width = 75)
        self.i = arcade.gui.UIFlatButton(text = "I", width = 75)
        self.j = arcade.gui.UIFlatButton(text = "J", width = 75)
        self.k = arcade.gui.UIFlatButton(text = "K", width = 75)
        self.l = arcade.gui.UIFlatButton(text = "L", width = 75)
        self.m = arcade.gui.UIFlatButton(text = "M", width = 75)
        self.n = arcade.gui.UIFlatButton(text = "N", width = 75)
        self.o = arcade.gui.UIFlatButton(text = "O", width = 75)
        self.p = arcade.gui.UIFlatButton(text = "P", width = 75)
        self.q = arcade.gui.UIFlatButton(text = "Q", width = 75)
        self.r = arcade.gui.UIFlatButton(text = "R", width = 75)
        self.s = arcade.gui.UIFlatButton(text = "S", width = 75)
        self.t = arcade.gui.UIFlatButton(text = "T", width = 75)
        self.u = arcade.gui.UIFlatButton(text = "U", width = 75)
        self.v = arcade.gui.UIFlatButton(text = "V", width = 75)
        self.w = arcade.gui.UIFlatButton(text = "W", width = 75)
        self.x = arcade.gui.UIFlatButton(text = "X", width = 75)
        self.y = arcade.gui.UIFlatButton(text = "Y", width = 75)
        self.z = arcade.gui.UIFlatButton(text = "Z", width = 75)

        #Add to Manager
        self.manager.add(self.a)
        self.manager.add(self.b)
        self.manager.add(self.c)
        self.manager.add(self.d)
        self.manager.add(self.e)
        self.manager.add(self.f)
        self.manager.add(self.g)
        self.manager.add(self.h)
        self.manager.add(self.i)
        self.manager.add(self.j)
        self.manager.add(self.k)
        self.manager.add(self.l)
        self.manager.add(self.m)
        self.manager.add(self.n)
        self.manager.add(self.o)
        self.manager.add(self.p)
        self.manager.add(self.q)
        self.manager.add(self.r)
        self.manager.add(self.s)
        self.manager.add(self.t)
        self.manager.add(self.u)
        self.manager.add(self.v)
        self.manager.add(self.w)
        self.manager.add(self.x)
        self.manager.add(self.y)
        self.manager.add(self.z)

        #Add buttons to layouts
        self.h_box1.add(self.q.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.w.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.e.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.r.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.t.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.y.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.u.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.i.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.o.with_space_around(right = 10, left = 10))
        self.h_box1.add(self.p.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.a.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.s.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.d.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.f.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.g.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.h.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.j.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.k.with_space_around(right = 10, left = 10))
        self.h_box2.add(self.l.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.z.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.x.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.c.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.v.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.b.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.n.with_space_around(right = 10, left = 10))
        self.h_box3.add(self.m.with_space_around(right = 10, left = 10))

        #Add Horizontal boxes to manager
        self.manager.add(self.h_box1)
        self.manager.add(self.h_box2)
        self.manager.add(self.h_box3)

        #Add horizontal layouts to vertical layouts
        self.v_box.add(self.h_box1.with_space_around(top = 10, bottom = 10))
        self.v_box.add(self.h_box2.with_space_around(top = 10, bottom = 10))
        self.v_box.add(self.h_box3.with_space_around(top = 10, bottom = 10))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "center_x",
                align_y = -150,
                child = self.v_box
            )
        )

        @self.a.event("on_click")
        def a_clicked(event):
            self.a_interact()

        @self.b.event("on_click")
        def b_clicked(event):
            self.b_interact()

        @self.c.event("on_click")
        def c_clicked(event):
            self.c_interact()
        
        @self.d.event("on_click")
        def d_clicked(event):
            self.d_interact()

        @self.e.event("on_click")
        def e_clicked(event):
            self.e_interact()

        @self.f.event("on_click")
        def f_clicked(event):
            self.f_interact()

        @self.g.event("on_click")
        def g_clicked(event):
            self.g_interact()

        @self.h.event("on_click")
        def h_clicked(event):
            self.h_interact()
        
        @self.i.event("on_click")
        def i_clicked(event):
            self.i_interact()

        @self.j.event("on_click")
        def j_clicked(event):
            self.j_interact()

        @self.k.event("on_click")
        def k_clicked(event):
            self.k_interact()

        @self.l.event("on_click")
        def l_clicked(event):
            self.l_interact()

        @self.m.event("on_click")
        def m_clicked(event):
            self.m_interact()
        
        @self.n.event("on_click")
        def n_clicked(event):
            self.n_interact()

        @self.o.event("on_click")
        def o_clicked(event):
            self.o_interact()

        @self.p.event("on_click")
        def p_clicked(event):
            self.p_interact()

        @self.q.event("on_click")
        def q_clicked(event):
            self.q_interact()

        @self.r.event("on_click")
        def r_clicked(event):
            self.r_interact()
        
        @self.s.event("on_click")
        def s_clicked(event):
            self.s_interact()

        @self.t.event("on_click")
        def t_clicked(event):
            self.t_interact()

        @self.u.event("on_click")
        def u_clicked(event):
            self.u_interact()

        @self.v.event("on_click")
        def v_clicked(event):
            self.v_interact()

        @self.w.event("on_click")
        def w_clicked(event):
            self.w_interact()
        
        @self.x.event("on_click")
        def x_clicked(event):
            self.x_interact()

        @self.y.event("on_click")
        def y_clicked(event):
            self.y_interact()

        @self.z.event("on_click")
        def z_clicked(event):
            self.z_interact()

        arcade.set_background_color(arcade.color.BLACK)

    def a_interact(self):
        if self.a.text not in self.used:
            self.used.append(self.a.text)
            self.check(self.a.text, self.word, self.hidden)
            self.game()
    
    def b_interact(self):
        if self.b.text not in self.used:
            self.used.append(self.b.text)
            self.check(self.b.text, self.word, self.hidden)
            self.game()

    def c_interact(self):
        if self.c.text not in self.used:
            self.used.append(self.c.text)
            self.check(self.c.text, self.word, self.hidden)
            self.game()

    def d_interact(self):
        if self.d.text not in self.used:
            self.used.append(self.d.text)
            self.check(self.d.text, self.word, self.hidden)
            self.game()

    def e_interact(self):
        if self.e.text not in self.used:
            self.used.append(self.e.text)
            self.check(self.e.text, self.word, self.hidden)
            self.game()
    
    def f_interact(self):
        if self.f.text not in self.used:
            self.used.append(self.f.text)
            self.check(self.f.text, self.word, self.hidden)
            self.game()

    def g_interact(self):
        if self.g.text not in self.used:
            self.used.append(self.g.text)
            self.check(self.g.text, self.word, self.hidden)
            self.game()

    def h_interact(self):
        if self.h.text not in self.used:
            self.used.append(self.h.text)
            self.check(self.h.text, self.word, self.hidden)
            self.game()
    
    def i_interact(self):
        if self.i.text not in self.used:
            self.used.append(self.i.text)
            self.check(self.i.text, self.word, self.hidden)
            self.game()

    def j_interact(self):
        if self.j.text not in self.used:
            self.used.append(self.j.text)
            self.check(self.j.text, self.word, self.hidden)
            self.game()
    
    def k_interact(self):
        if self.k.text not in self.used:
            self.used.append(self.k.text)
            self.check(self.k.text, self.word, self.hidden)
            self.game()

    def l_interact(self):
        if self.l.text not in self.used:
            self.used.append(self.l.text)
            self.check(self.l.text, self.word, self.hidden)
            self.game()

    def m_interact(self):
        if self.m.text not in self.used:
            self.used.append(self.m.text)
            self.check(self.m.text, self.word, self.hidden)
            self.game()
    
    def n_interact(self):
        if self.n.text not in self.used:
            self.used.append(self.n.text)
            self.check(self.n.text, self.word, self.hidden)
            self.game()

    def o_interact(self):
        if self.o.text not in self.used:
            self.used.append(self.o.text)
            self.check(self.o.text, self.word, self.hidden)
            self.game()
    
    def p_interact(self):
        if self.p.text not in self.used:
            self.used.append(self.p.text)
            self.check(self.p.text, self.word, self.hidden)
            self.game()

    def q_interact(self):
        if self.q.text not in self.used:
            self.used.append(self.q.text)
            self.check(self.q.text, self.word, self.hidden)
            self.game()

    def r_interact(self):
        if self.r.text not in self.used:
            self.used.append(self.r.text)
            self.check(self.r.text, self.word, self.hidden)
            self.game()
    
    def s_interact(self):
        if self.s.text not in self.used:
            self.used.append(self.s.text)
            self.check(self.s.text, self.word, self.hidden)
            self.game()

    def t_interact(self):
        if self.t.text not in self.used:
            self.used.append(self.t.text)
            self.check(self.t.text, self.word, self.hidden)
            self.game()
    
    def u_interact(self):
        if self.u.text not in self.used:
            self.used.append(self.u.text)
            self.check(self.u.text, self.word, self.hidden)
            self.game()

    def v_interact(self):
        if self.v.text not in self.used:
            self.used.append(self.v.text)
            self.check(self.v.text, self.word, self.hidden)
            self.game()

    def w_interact(self):
        if self.w.text not in self.used:
            self.used.append(self.w.text)
            self.check(self.w.text, self.word, self.hidden)
            self.game()
    
    def x_interact(self):
        if self.x.text not in self.used:
            self.used.append(self.x.text)
            self.check(self.x.text, self.word, self.hidden)
            self.game()
    
    def y_interact(self):
        if self.y.text not in self.used:
            self.used.append(self.y.text)
            self.check(self.y.text, self.word, self.hidden)
            self.game()

    def z_interact(self):
        if self.z.text not in self.used:
            self.used.append(self.z.text)
            self.check(self.z.text, self.word, self.hidden)
            self.game()

    def setup(self):
        self.words = ["algebra", "horrific", "nightmare", "finite", "independent", "marvelous", "spectacular", "incomprehensible", "serendipity", "miraculous", "zany", "cumbersome", "apalled", "vegetarian"] 
        self.word = self.words[random.randint(0, len(self.words) - 1)]

        self.used = []
        self.hidden = []
        self.guesses = 5
        self.letter = None

        for i in range(len(self.word)):
            self.hidden.append("_")
        
        self.game()

    def game(self):
        if self.guesses > 0:
            print(str(self.guesses) + " guesses left")
            print(" ".join(self.hidden))
            os.system('clear')
                    
            if self.win(self.hidden, self.word) == True:
                self.score += 1
                if self.score > self.high_score:
                    self.high_score = self.score
                
                round_over_screen = RoundOver(self.score, self.high_score)
                self.window.show_view(round_over_screen)
                
        else:
            game_over_screen = GameOver(self.score, self.high_score)
            self.window.show_view(game_over_screen)

    def check(self, l, w, h):
        found = 0
        for i in range(len(w)):
            if l.lower() == w[i]:
                found += 1
                h[i] = l.lower()

        if found > 0:
            return True
        else:
            self.guesses -= 1
            return False
        
    def win(self, h, w):
        if "".join(h) == w:
            return True
    
    def on_draw(self):

        self.clear()

        self.manager.draw()

        #Appears at start
        arcade.draw_line(720, 755, 720, 725, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 720, 755, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 625, 455, arcade.color.WHITE, 1)
        arcade.draw_line(580, 455, 860, 455, arcade.color.WHITE, 1)


        if self.guesses <= 4:
            arcade.draw_circle_outline(720, 675, 50, arcade.color.WHITE)
            arcade.draw_circle_outline(720, 650, 10, arcade.color.WHITE)
            arcade.draw_line(710, 690, 690, 670, arcade.color.WHITE, 1)
            arcade.draw_line(710, 670, 690, 690, arcade.color.WHITE, 1)
            arcade.draw_line(750, 690, 730, 670, arcade.color.WHITE, 1)
            arcade.draw_line(750, 670, 730, 690, arcade.color.WHITE, 1)
            arcade.draw_line(720, 625, 720, 525, arcade.color.WHITE, 1)

        if self.guesses <= 3:
            arcade.draw_line(720, 525, 690, 475, arcade.color.WHITE, 1)

        if self.guesses <= 2:
            arcade.draw_line(720, 525, 750, 475, arcade.color.WHITE, 1)

        if self.guesses <= 1:
            arcade.draw_line(720, 600, 750, 550, arcade.color.WHITE, 1)

        if self.guesses == 0:
            arcade.draw_line(720, 600, 690, 550, arcade.color.WHITE, 1)

        arcade.draw_text(" ".join(self.hidden), 720, 400, arcade.color.WHITE, 50, anchor_x = "center", anchor_y = "center")
        arcade.draw_text("Used: " + " ".join(self.used), 900, 700, arcade.color.WHITE, 20)

    def on_key_press(self, symbol, modifiers):
        """Handles user input
        Letter Keys: Whatever key was pressed was entered as guess
        ESC: Quit the game"""

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.A:
            self.a_interact()

        if symbol == arcade.key.B:
            self.b_interact()

        if symbol == arcade.key.C:
            self.c_interact()

        if symbol == arcade.key.D:
            self.d_interact()

        if symbol == arcade.key.E:
            self.e_interact()

        if symbol == arcade.key.F:
            self.f_interact()

        if symbol == arcade.key.G:
            self.g_interact()

        if symbol == arcade.key.H:
            self.h_interact()

        if symbol == arcade.key.I:
            self.i_interact()

        if symbol == arcade.key.J:
            self.j_interact()

        if symbol == arcade.key.K:
            self.k_interact()

        if symbol == arcade.key.L:
            self.l_interact()

        if symbol == arcade.key.M:
            self.m_interact()

        if symbol == arcade.key.N:
            self.n_interact()

        if symbol == arcade.key.O:
            self.o_interact()

        if symbol == arcade.key.P:
            self.p_interact()

        if symbol == arcade.key.Q:
            self.q_interact()

        if symbol == arcade.key.R:
            self.r_interact()

        if symbol == arcade.key.S:
            self.s_interact()

        if symbol == arcade.key.T:
            self.t_interact()

        if symbol == arcade.key.U:
            self.u_interact()

        if symbol == arcade.key.V:
            self.v_interact()

        if symbol == arcade.key.W:
            self.w_interact()

        if symbol == arcade.key.X:
            self.x_interact()

        if symbol == arcade.key.Y:
            self.y_interact()

        if symbol == arcade.key.Z:
            self.z_interact()

    def on_update(self, delta_time):
        self.manager.on_update(delta_time)

#Game over screen
class GameOver(arcade.View):
    
    def __init__(self, c_score, h_score):
        super().__init__()
        self.c_score = c_score
        self.h_score = h_score

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()

        arcade.draw_circle_outline(720, 675, 50, arcade.color.WHITE)
        arcade.draw_circle_outline(720, 650, 10, arcade.color.WHITE)
        arcade.draw_line(710, 690, 690, 670, arcade.color.WHITE, 1)
        arcade.draw_line(710, 670, 690, 690, arcade.color.WHITE, 1)
        arcade.draw_line(750, 690, 730, 670, arcade.color.WHITE, 1)
        arcade.draw_line(750, 670, 730, 690, arcade.color.WHITE, 1)
        arcade.draw_line(720, 755, 720, 725, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 720, 755, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 625, 455, arcade.color.WHITE, 1)
        arcade.draw_line(580, 455, 860, 455, arcade.color.WHITE, 1)
        arcade.draw_line(720, 625, 720, 525, arcade.color.WHITE, 1)
        arcade.draw_line(720, 525, 690, 475, arcade.color.WHITE, 1)
        arcade.draw_line(720, 525, 750, 475, arcade.color.WHITE, 1)
        arcade.draw_line(720, 600, 750, 550, arcade.color.WHITE, 1)
        arcade.draw_line(720, 600, 690, 550, arcade.color.WHITE, 1)

        arcade.draw_text("Game Over!", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size = 50, anchor_x = "center")
        arcade.draw_text("Final Score: " + str(self.c_score), self.window.width / 2, self.window.height / 2.5, arcade.color.WHITE, font_size = 30, anchor_x = "center")
        arcade.draw_text("High Score: " + str(self.h_score), 1100, 700, arcade.color.WHITE, font_size = 30)
        arcade.draw_text("Press enter/return to play again", self.window.width / 2, self.window.height / 3, arcade.color.WHITE, font_size = 20, anchor_x = "center")

    def on_key_press(self, symbol, modifiers):
        """Handles user input
        Letter Keys: Whatever key was pressed was entered as guess
        ESC: Quit the game
        ENTER: Start New Game"""

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.ENTER:
            play_screen = PlayScreen(initial_score = 0, all_time = self.h_score)
            play_screen.setup()
            self.window.show_view(play_screen)

#Round over screen
class RoundOver(arcade.View):
    
    def __init__(self, c_score, h_score):
        super().__init__()
        self.c_score = c_score
        self.h_score = h_score

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):

        self.clear()

        arcade.draw_circle_outline(720, 670, 30, arcade.color.WHITE)
        arcade.draw_lrtb_rectangle_filled(600, 780, 720, 650, arcade.color.BLACK)
        arcade.draw_circle_outline(720, 675, 50, arcade.color.WHITE)
        arcade.draw_circle_filled(700, 680, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(740, 680, 10, arcade.color.WHITE)
        arcade.draw_circle_filled(700, 680, 5, arcade.color.BLACK)
        arcade.draw_circle_filled(740, 680, 5, arcade.color.BLACK)
        arcade.draw_line(720, 755, 720, 725, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 720, 755, arcade.color.WHITE, 1)
        arcade.draw_line(625, 755, 625, 455, arcade.color.WHITE, 1)
        arcade.draw_line(580, 455, 860, 455, arcade.color.WHITE, 1)
        arcade.draw_line(720, 625, 720, 525, arcade.color.WHITE, 1)
        arcade.draw_line(720, 525, 690, 475, arcade.color.WHITE, 1)
        arcade.draw_line(720, 525, 750, 475, arcade.color.WHITE, 1)
        arcade.draw_line(720, 600, 750, 550, arcade.color.WHITE, 1)
        arcade.draw_line(720, 600, 690, 550, arcade.color.WHITE, 1)

        arcade.draw_text("You Win!", self.window.width / 2, self.window.height / 2, arcade.color.WHITE, font_size = 50, anchor_x = "center")
        arcade.draw_text("Score: " + str(self.c_score), self.window.width / 2, self.window.height / 2.5, arcade.color.WHITE, font_size = 30, anchor_x = "center")
        arcade.draw_text("High Score: " + str(self.h_score), 1100, 700, arcade.color.WHITE, font_size = 30)
        arcade.draw_text("Press enter/return to play again", self.window.width / 2, self.window.height / 3, arcade.color.WHITE, font_size = 20, anchor_x = "center")

    def on_key_press(self, symbol, modifiers):
        """Handles user input
        Letter Keys: Whatever key was pressed was entered as guess
        ESC: Quit the game
        ENTER: Start New Game"""

        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

        if symbol == arcade.key.ENTER:
            play_screen = PlayScreen(initial_score = self.c_score, all_time = self.h_score)
            play_screen.setup()
            self.window.show_view(play_screen)

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = Start()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()