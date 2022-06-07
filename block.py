import tkinter as tk
import math
import pygame as pg
import random as rd
from PIL import ImageTk

NUM_H_BLOCK = 10  # ブロックの数（横方向)
NUM_V_BLOCK = 10  # ブロックの数（縦方向）
WIDTH_BLOCK = 100  # ブロックの幅
HEIGHT_BLOCK = 30  # ブロックの高さ
COLOR_BLOCK = "blue"  # ブロックの色

HEIGHT_SPACE = 400  # 縦方向の空きスペース

WIDTH_PADDLE = 200  # パドルの幅
HEIGHT_PADDLE = 20  # パドルの高さ
Y_PADDLE = 50  # パドルの下方向からの位置
COLOR_PADDLE = "green"  # パドルの色

RADIUS_BALL = 10  # ボールの半径
COLOR_BALL = "red"  # ボールの色
NUM_BALL = 1  # ボールの数

UPDATE_TIME = 20  # 更新間隔（ms）

START_GAME=False
GAME_FINISH=False
CLEAR_GAME=False
OVER_GAME=False


LEBEL_S="EASY"#難易度設定
LEBEL_C=(0,255,0)#スタートボタンの色
SCORE=0#ブロックを破壊したポイント
BONUS=0#床にぶつからずに連続でブロックを破壊
PDBO=False#床にボールが当たったか
BG_PG="fig/pg_bg.jpg"#背景


MARIO=[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,2,2,2,2,0,0,0,0],
        [0,2,2,2,2,2,2,2,2,2],
        [0,1,1,1,3,1,3,3,0,0],
        [1,3,1,3,3,1,3,3,0,0],
        [1,3,1,3,3,1,3,3,3,0],
        [1,3,1,3,3,3,1,3,3,3],
        [1,1,3,3,3,1,1,1,1,0],
        [0,0,3,3,3,3,3,0,0,0]]
DIAMOND=[[0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1,1,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
PRAMID=[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,0,1,1,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,1,1,0],
        [0,1,1,1,1,1,1,1,1,0],
        [1,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1]]
ONESTROKE=[[0,1,1,0,0,1,1,0,1,1],
        [1,1,0,1,0,1,1,0,0,0],
        [1,1,0,1,0,1,1,1,1,0],
        [1,0,0,1,0,0,1,1,1,0],
        [1,0,1,1,0,1,1,1,1,0],
        [1,1,1,1,0,1,1,1,1,0],
        [1,1,1,1,0,1,1,1,1,0],
        [1,1,1,1,0,1,0,1,1,1],
        [0,1,1,1,0,1,0,0,0,0],
        [0,1,1,1,0,0,0,1,1,0]]

VIRUS=[[0,0,0,1,1,0,0,0],
        [0,0,1,1,1,1,0,0],
        [0,1,1,1,1,1,1,0],
        [1,1,0,1,1,0,1,1],
        [1,1,1,1,1,1,1,1],
        [0,0,1,0,0,1,0,0],
        [0,1,0,1,1,0,1,0],
        [1,0,1,0,0,1,0,1]]

tms=0
tms2=True

class Ball:
    def __init__(self, x, y, radius, x_min, y_min, x_max, y_max):
        '''ボール作成'''

        # 位置と半径と移動可能範囲を設定
        self.x = x
        self.y = y
        self.r = radius
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        # 一度に移動する距離（px）
        self.speed = 10

        # 移動方向を設定
        self.angle = math.radians(30)
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

    def getCoords(self):
        '''左上の座標と右下の座標の取得'''

        return (self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        '''移動'''

        # 移動方向に移動
        # self.x += self.dx
        # self.y += self.dy
        if LEBEL_S!= "Nightmare":
            self.x += self.dx
        elif LEBEL_S=="Nightmare":
            self.x += self.dx*1.5#New
        if LEBEL_S!= "Nightmare":
            self.y += self.dy
        elif LEBEL_S=="Nightmare":
            self.y += self.dy*1.5#New

        if self.x < self.x_min:
            # 左の壁とぶつかった

            # 横方向に反射
            self.reflectH()
            self.x = self.x_min

        elif self.x > self.x_max:
            # 右の壁とぶつかった

            # 横方向に反射
            self.reflectH()
            self.x = self.x_max

        if self.y < self.y_min:
            # 上の壁とぶつかった

            # 縦方向に反射
            self.reflectV()
            self.y = self.y_min

        # elif self.y > self.y_max:
        #     #下の壁とぶつかった

        #     #縦方向に反射
        #     self.reflectV()
        #     self.y = self.y_max

    def turn(self, angle):
        '''移動方向をangleに応じて設定'''

        self.angle = angle
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

    def reflectH(self):
        '''横方向に対して反射'''

        self.turn(math.atan2(self.dy, -self.dx))

    def reflectV(self):
        '''縦方向に対して反射'''

        self.turn(math.atan2(-self.dy, self.dx))

    def getCollisionCoords(self, object):
        '''objectと当たった領域の座標の取得'''

        # 各オブジェクトの座標を取得
        ball_x1, ball_y1, ball_x2, ball_y2 = self.getCoords()
        object_x1, object_y1, object_x2, object_y2 = object.getCoords()

        # 新たな矩形の座標を取得
        x1 = max(ball_x1, object_x1)
        y1 = max(ball_y1, object_y1)
        x2 = min(ball_x2, object_x2)
        y2 = min(ball_y2, object_y2)

        if x1 < x2 and y1 < y2:
            # 始点が終点よりも左上にある

            # 当たった領域の左上座標と右上座標を返却
            return (x1, y1, x2, y2)
        else:

            # 当たっていないならNoneを返却
            return None

    def reflect(self, object):
        '''当たった方向に応じて反射'''

        # 各オブジェクトの座標を取得
        object_x1, object_y1, object_x2, object_y2 = object.getCoords()

        # 重なった領域の座標を取得
        x1, y1, x2, y2 = self.getCollisionCoords(object)

        is_collideV = False
        is_collideH = False

        # どの方向からボールが当たったかを判断
        if self.dx < 0:
            # ボールが左方向に移動中
            if x2 == object_x2:
                # objectの左側と当たった
                is_collideH = True
        else:
            # ボールが右方向に移動中
            if x1 == object_x1:
                # objectの右側と当たった
                is_collideH = True

        if self.dy < 0:
            # ボールが上方向に移動中
            if y2 == object_y2:
                # objectの下側と当たった
                is_collideV = True
        else:
            # ボールが下方向に移動中
            if y1 == object_y1:
                # objectの上側と当たった
                is_collideV = True

        if is_collideV and is_collideH:
            # 横方向と縦方向両方から当たった場合
            if x2 - x1 > y2 - y1:
                # 横方向の方が重なりが大きいので横方向に反射
                self.reflectV()
            elif x2 - x1 < y2 - y1:
                # 縦方向の方が重なりが大きいので縦方向に反射
                self.reflectH()
            else:
                # 両方同じなので両方向に反射
                self.reflectH()
                self.reflectV()

        elif is_collideV:
            # 縦方向のみ当たったので縦方向に反射
            self.reflectV()

        elif is_collideH:
            # 横方向のみ当たったので横方向に反射
            self.reflectH()

    def exists(self):
        '''画面内に残っているかどうかの確認'''

        return True if self.y <= self.y_max else False


class Paddle:
    def __init__(self, x, y, width, height, x_min, y_min, x_max, y_max):
        '''パドル作成'''

        # 中心座標と半径と移動可能範囲を設定
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

    def getCoords(self):
        '''左上の座標と右下の座標の取得'''

        return (self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2)

    def move(self, mouse_x, mouse_y):
        '''(mouse_x, mouse_y) に移動'''

        # 移動可能範囲で移動
        self.x = min(max(mouse_x, self.x_min), self.x_max)
        self.y = min(max(mouse_y, self.y_min), self.y_max)


class Block:

    def __init__(self, x, y, width, height):
        '''ブロック作成'''

        # 中心座標とサイズを設定
        self.x = x
        self.y = y
        self.w = width
        self.h = height

    def getCoords(self):
        '''左上の座標と右下の座標の取得'''

        return (self.x - self.w / 2, self.y - self.h / 2, self.x + self.w / 2, self.y + self.h / 2)



class Breakout:
    global tms,tms2,PDBO,GAME_FINISH

    def __init__(self, master):
        '''ブロック崩しゲーム起動'''
        self.master = master

        # サイズを設定
        self.width = NUM_H_BLOCK * WIDTH_BLOCK
        self.height = NUM_V_BLOCK * HEIGHT_BLOCK + HEIGHT_SPACE

        # ゲーム開始フラグを設定
        self.is_playing = False

        self.createWidgets()
        self.createObjects()
        self.drawFigures()
        self.setEvents()

    def start(self, event):
        '''ゲーム開始'''

        if len(self.blocks) == 0 or len(self.balls) == 0:
            # ゲームクリア or ゲームオーバー時は最初からやり直し

            # キャンバスの図形を全て削除
            self.canvas.delete("all")

            # 全オブジェクトの作り直しと図形描画
            self.createObjects()
            self.drawFigures()

        # ゲーム開始していない場合はゲーム開始
        if not self.is_playing:#New
            self.is_playing = True
            music("1")
            self.loop()
        # else:
        #     self.is_playing = False

    def loop(self):
        '''ゲームのメインループ'''
        global PDBO


        if not self.is_playing:
            # ゲーム開始していないなら何もしない
            return
        
        if tms>0:
            self.canvas.delete("times")
        #New
        #self.canvas.create_text(50,400,text=tms,anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="black",tag="times")
        
        if LEBEL_S=="Nightmare":
            self.canvas.create_text(50,500,text="スコア",anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="blue",tag="times")
            self.canvas.create_text(50,600,text=SCORE,anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="blue",tag="times")
        elif LEBEL_S=="EASY":
            self.canvas.create_text(30,300,text="スコア",anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="red",tag="times")
            self.canvas.create_text(50,400,text=SCORE,anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="red",tag="times")
        elif LEBEL_S=="HARD":
            self.canvas.create_text(30,300,text="スコア",anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="yellow",tag="times")
            self.canvas.create_text(50,400,text=SCORE,anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="yellow",tag="times")
        else:
            self.canvas.create_text(50,500,text="スコア",anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="black",tag="times")
            self.canvas.create_text(50,600,text=SCORE,anchor="sw",font=("HG丸ゴシックM-PRO",24),fill="black",tag="times")
        

        # loopをUPDATE_TIME ms後に再度実行
        self.master.after(UPDATE_TIME, self.loop)

        # 全ボールを移動する
        for ball in self.balls:
            ball.move()
        

        # ボールが画面外に出たかどうかをチェック
        delete_balls = []
        for ball in self.balls:
            if not ball.exists():
                # 外に出たボールは削除対象リストに入れる
                delete_balls.append(ball)

        for ball in delete_balls:
            # 削除対象リストのボールを削除
            self.delete(ball)

        self.collision()
        self.updateFigures()
        self.result()
        if GAME_FINISH==True:#New
            self.master.destroy()#Breakoutクラスの強制終了

    def motion(self, event):
        '''パドルの移動'''

        self.paddle.move(event.x, event.y)

    def delete(self, target):
        '''targetのオブジェクトと図形を削除'''

        # 図形IDを取得してキャンバスから削除
        figure = self.figs.pop(target)
        self.canvas.delete(figure)

        # targetを管理リストから削除
        if isinstance(target, Ball):
            self.balls.remove(target)
        elif isinstance(target, Block):
            self.blocks.remove(target)

    def collision(self):
        '''当たり判定と当たった時の処理'''
        global PDBO

        for ball in  self.balls:

            collided_block = None  # 一番大きく当たったブロック
            max_area = 0  # 一番大きな当たった領域

            for block in self.blocks:

                # ballとblockとの当たった領域の座標を取得
                collision_rect = ball.getCollisionCoords(block)#New
                if collision_rect is not None:
                    music("2")
                    # 当たった場合

                    # 当たった領域の面積を計算
                    x1, y1, x2, y2 = collision_rect
                    area = (x2 - x1) * (y2 - y1)

                    # 一番大きく当たっているかどうかを判断
                    if area > max_area:
                        # 一番大きく当たった領域の座標を覚えておく
                        max_area = area

                        # 一番大きく当たったブロックを覚えておく
                        collided_block = block

            if collided_block is not None:

                # 一番大きく当たったブロックに対してボールを反射
                ball.reflect(collided_block)
                score()#New

                # 一番大きく当たったブロックを削除
                self.delete(collided_block)

            for another_ball in self.balls:
                if another_ball is ball:
                    # 同じボールの場合はスキップ
                    continue

                # ballとanother_ballとの当たり判定
                if ball.getCollisionCoords(another_ball) is not None:

                    # 当たってたらballを反射
                    ball.reflect(another_ball)

            # ballとself.paddleとの当たり判定
            if ball.getCollisionCoords(self.paddle) is not None:


                # 当たってたらballを反射
                ball.reflect(self.paddle)
                PDBO=True#New

    def result(self):
        global tms2,GAME_FINISH,CLEAR_GAME,OVER_GAME
        '''ゲームの結果を表示する'''

        if len(self.blocks) == 0:#New
            tms2=False
            music_sp()
            GAME_FINISH=True
            CLEAR_GAME=True
            # self.canvas.create_text(
            #     self.width // 2, self.height // 2,
            #     text="GAME CLEAR",
            #     font=("", 40),
            #     fill="blue"
            # )

            self.is_playing = False

        if len(self.balls) == 0:#New
            music_sp()
            tms2=False
            GAME_FINISH=True
            OVER_GAME=True
            # self.canvas.create_text(
            #     self.width // 2, self.height // 2,
            #     text="GAME OVER",
            #     font=("", 40),
            #     fill="red"
            # )
            

            self.is_playing = False

    def setEvents(self):
        '''イベント受付設定'''
        
        self.canvas.bind("<ButtonPress>", self.start)
        self.canvas.bind("<Motion>", self.motion)

    def createWidgets(self):
        '''必要なウィジェットを作成'''
        self.imgage = ImageTk.PhotoImage(file=BG_PG)#New

        # キャンバスを作成
        self.canvas = tk.Canvas(
            self.master,
            width=self.width,
            height=self.height,
            highlightthickness=0,
            bg="gray"
        )
        self.canvas.pack(padx=10, pady=10)
        
        self.canvas.create_image(
            self.width/2,
            self.height/2,
            image = self.imgage
        )

    def createObjects(self):
        '''ゲームに登場するオブジェクトを作成'''

        # ボールを作成
        self.balls = []
        for i in range(NUM_BALL):
            x = self.width / NUM_BALL * i + self.width / NUM_BALL / 2
            ball = Ball(
                x, self.height // 2,
                RADIUS_BALL,
                RADIUS_BALL, RADIUS_BALL,
                self.width - RADIUS_BALL, self.height - RADIUS_BALL
            )
            self.balls.append(ball)

        # パドルを作成
        self.paddle = Paddle(
            self.width // 2, self.height - Y_PADDLE,
            WIDTH_PADDLE, HEIGHT_PADDLE,
            WIDTH_PADDLE // 2, self.height - Y_PADDLE,
            self.width - WIDTH_PADDLE // 2, self.height - Y_PADDLE
        )

        # ブロックを作成
        self.blocks = []#New
        self.blockslis=[]
        if LEBEL_S=="EASY":
            for v in range(NUM_V_BLOCK):
                for h in range(NUM_H_BLOCK):
                    if MARIO[v][h]!=0:
                        block = Block(
                            h * WIDTH_BLOCK + WIDTH_BLOCK // 2,
                            v * HEIGHT_BLOCK + HEIGHT_BLOCK // 2,
                            WIDTH_BLOCK,
                            HEIGHT_BLOCK
                        )
                        self.blocks.append(block)
                        self.blockslis.append(MARIO[v][h])
        if LEBEL_S=="NORMAL":
            for v in range(NUM_V_BLOCK):
                for h in range(NUM_H_BLOCK):
                    if PRAMID[v][h]!=0:
                        block = Block(
                            h * WIDTH_BLOCK + WIDTH_BLOCK // 2,
                            v * HEIGHT_BLOCK + HEIGHT_BLOCK // 2,
                            WIDTH_BLOCK,
                            HEIGHT_BLOCK
                        )
                        self.blocks.append(block)
            block = Block(
                4.5 * WIDTH_BLOCK + WIDTH_BLOCK // 2,
                0 * HEIGHT_BLOCK + HEIGHT_BLOCK // 2,
                WIDTH_BLOCK,
                HEIGHT_BLOCK
            )
            self.blocks.append(block)
            
        if LEBEL_S=="HARD":
            for v in range(NUM_V_BLOCK):
                for h in range(NUM_H_BLOCK):
                    if ONESTROKE[v][h]!=0:
                        block = Block(
                            h * WIDTH_BLOCK + WIDTH_BLOCK // 2,
                            v * HEIGHT_BLOCK + HEIGHT_BLOCK // 2,
                            WIDTH_BLOCK,
                            HEIGHT_BLOCK
                        )
                        self.blocks.append(block)
                        
        if LEBEL_S=="Nightmare":
            for v in range(NUM_V_BLOCK):
                for h in range(NUM_H_BLOCK):
                    if VIRUS[v][h]!=0:
                        block = Block(
                            h * WIDTH_BLOCK + WIDTH_BLOCK // 2,
                            v * HEIGHT_BLOCK + HEIGHT_BLOCK // 2,
                            WIDTH_BLOCK,
                            HEIGHT_BLOCK
                        )
                        self.blocks.append(block)
                        self.blockslis.append([VIRUS[v][h],2])
                    else:
                        self.blockslis.append([VIRUS[v][h],-1])

    def drawFigures(self):
        '''各オブジェクト毎に図形を描画'''

        # オブジェクト図形を関連づける辞書
        self.figs = {}

        # ボールを描画
        for ball in self.balls:
            x1, y1, x2, y2 = ball.getCoords()
            figure = self.canvas.create_oval(
                x1, y1, x2, y2,
                fill=COLOR_BALL
            )
            self.figs[ball] = figure

        # パドルを描画
        x1, y1, x2, y2 = self.paddle.getCoords()
        figure = self.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=COLOR_PADDLE
        )
        self.figs[self.paddle] = figure

        # ブロックを描画
        if LEBEL_S=="EASY":
            for block in range(len(self.blocks)):
                if self.blockslis[block]==1:
                    COLOR_FILL="black"
                elif self.blockslis[block]==2:
                    COLOR_FILL="red"
                elif self.blockslis[block]==3:
                    COLOR_FILL="blanched almond"
                x1, y1, x2, y2 = self.blocks[block].getCoords()
                figure = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=COLOR_FILL
                )
                self.figs[self.blocks[block]] = figure
        else:
            for block in range(len(self.blocks)):
                x1, y1, x2, y2 = self.blocks[block].getCoords()
                figure = self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=COLOR_BLOCK
                )
                self.figs[self.blocks[block]] = figure
        


    def updateFigures(self):
        '''新しい座標に図形を移動'''
        

        # ボールの座標を変更
        for ball in self.balls:
            x1, y1, x2, y2 = ball.getCoords()
            figure = self.figs[ball]
            self.canvas.coords(figure, x1, y1, x2, y2)

        # パドルの座標を変更
        x1, y1, x2, y2 = self.paddle.getCoords()
        figure = self.figs[self.paddle]
        self.canvas.coords(figure, x1, y1, x2, y2)
        

def count_up():
    global tms ,tms2
    if tms2==True:
        tms +=1
    app.after(1000,count_up)
    
def score():#New
    global SCORE, BONUS,PDBO
    if PDBO==False:
        BONUS+=1
    else:
        BONUS=0
        PDBO=False
    SCORE+= (1+BONUS*(rd.randint(1,10)))
    return

def start_screen():#New
    global START_GAME,LEBEL_S,LEBEL_C
    WIDTH = 600
    HEIGHT = 500
    green=(0,255,0)
    yellow=(255,255,0)
    red=(255,0,0)
    pup=(158,0,158)
    pup_ct=0
    screen = pg.display.set_mode((WIDTH,HEIGHT))    # 大きさ600*500の画面を生成
    pg.display.set_caption("ブロック崩し")              # タイトルバーに表示する文字
    pg.mixer.music.load("./Lastkadai/fig2/セレクト画面.mp3") 
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生
    font = pg.font.Font("./Lastkadai/ipaexg.ttf", 55)               # フォントの設定(55px)
    font2 = pg.font.Font("./Lastkadai/ipaexg.ttf", 30) 
    screen.fill((137,189,222))                                    # 画面を空色に塗りつぶし
    button1 = pg.Rect(200, 300, 200, 100)        #ボタンもどきを生成
    text1 = font.render("START", True, (0,0,0)) #ボタンの文字を作成
    
    button2 = pg.Rect(120, 200, 75, 30)    #160 
    text2 = font2.render("EASY", True, (0,0,0))
    button3 = pg.Rect(235, 200, 130, 30)  #235~365   
    text3 = font2.render("NORMAL", True, (0,0,0))
    button4 = pg.Rect(405, 200, 85, 30)     
    text4 = font2.render("HARD", True, (0,0,0))
    button5 = pg.Rect(405, 200, 150, 30)     
    text5 = font2.render("Nightmare", True, (0,0,0))
    
    text = font.render("ブロック崩し", True, (128,128,255))   # 描画する文字列の設定
    text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2-100))#文字の中央の座標を取得
    
    hit=pg.mixer.Sound("./Lastkadai/fig2/決定、ボタン押下3.mp3")
    bs=pg.mixer.Sound("./Lastkadai/fig2/nc129702 ボス、モンスターの叫び声.mp3")
    cl=pg.mixer.Sound("./Lastkadai/fig2/決定、ボタン押下5.mp3")
    hit.set_volume(1.0)
    
    while True:
        pg.draw.rect(screen, LEBEL_C, button1)# 描画するボタンもどきの設定
        screen.blit(text1, (215, 325))          # 文字列の表示位置
        
        pg.draw.rect(screen, green, button2)
        screen.blit(text2, (120, 200))
        pg.draw.rect(screen, yellow, button3)
        screen.blit(text3, (235, 200))
        if pup_ct!=10:
            pg.draw.rect(screen,red, button4)
            screen.blit(text4, (405, 200))
        elif pup_ct==10:
            pg.draw.rect(screen,pup, button5)
            screen.blit(text5, (405, 200))
        
        
        screen.blit(text,text_rect)# 文字列の表示位置
        pg.display.update()     # 画面を更新
        # イベント処理
        for event in pg.event.get():
            
            msx,msy=pg.mouse.get_pos()#mouseの座標を取得
            
            msb=pg.mouse.get_pressed()#mouseのクリックを有無を取得 
            if LEBEL_S!="Nightmare":
                if  msb ==(True,False,False) and msx>=120 and msx<= 195 and msy<=230 and msy>= 200:#EASYボタンが押されたなら
                    hit.play()#ロードした音楽の再生
                    green=(0,225,0)
                    LEBEL_C=(0, 255, 0)
                    LEBEL_S="EASY"
                    pup_ct=0
                elif msb ==(True,False,False) and  msx>=235 and msx<= 365 and msy<=230 and msy>= 200:#NORMALボタンが押されたなら
                    hit.play()#ロードした音楽の再生
                    yellow=(225,225,0)
                    LEBEL_C=(255, 255, 0)
                    LEBEL_S="NORMAL"
                    pup_ct=0
                elif msb ==(True,False,False) and  msx>=405 and msx<= 490 and msy<=230 and msy>= 200 and pup_ct<=9:#HARDボタンが押されたなら
                    red=(225,0,0)
                    LEBEL_C=(255, 0, 0)
                    LEBEL_S="HARD"
                    pup_ct+=1
                    if pup_ct==10:
                        bs.play()
                        LEBEL_C=(128, 0, 128)
                        LEBEL_S="Nightmare"
                    else:
                        hit.play()#ロードした音楽の再生
            if msb ==(True,False,False) and  msx>=405 and msx<= 555 and msy<=230 and msy>= 200 and pup_ct>9:#HARDボタンが押されたなら
                pup=(128,0,128)
                LEBEL_C=(158, 0, 158)
                LEBEL_S="Nightmare"
                pup_ct=10
            if msb ==(False,False,False):
                green=(0,255,0)
                yellow=(255,255,0)
                red=(255,0,0)
                pup=(158,0,158)
            
            if msb ==(True,False,False) and msx>=200 and msx<= 400 and msy<=400 and msy>= 300:#もしマウスがスタートボタン範囲内でクリックしたら
                cl_l=cl.get_num_channels()
                if cl_l==0:
                    cl.play(maxtime=1400)
                cl_l=cl.get_num_channels()
                START_GAME=True
                if LEBEL_S=="EASY":
                    LEBEL_C=(0,225,0)
                elif LEBEL_S=="NORMAL":
                    LEBEL_C=(225, 225, 0)
                elif LEBEL_S=="HARD":
                    LEBEL_C=(225, 0, 0)
                elif LEBEL_S=="Nightmare":
                    LEBEL_C=(98,0,98)
            if msb ==(False,False,False) and START_GAME==True :
                while cl_l!=0:
                    cl_l=cl.get_num_channels()
                pg.mixer.music.stop()
                pg.quit()
                return
            if event.type == pg.QUIT:  # 閉じるボタンが押されたら終了
                return


def level(s):#New
    if s=="EASY":
        return 10,10,60,30,"blue",400,250,20,50,"green",15,"red",1 ,"./Lastkadai/fig2/easy_bg.png"
    elif s=="NORMAL":
        return 10,10,100,30,"sandy brown",400,200,20,50,"green",15,"red",1 ,"./Lastkadai/fig2/desert_bg.jpg"
    elif s=="HARD":
        return 10,10,100,30,"blue",400,100,20,50,"green",10,"red",1,"./Lastkadai/fig2/hard_bg.jpg"
    elif s=="Nightmare":
        return 8,8,50,50,"gray",320,80,20,50,"green",10,"red",1,"./Lastkadai/fig2/Nightmare_bg.jpg"

def clear_screen(point):#New
    WIDTH = 600
    HEIGHT = 500
    screen = pg.display.set_mode((WIDTH,HEIGHT))    # 大きさ600*500の画面を生成
    pg.display.set_caption("GAMECLEAR")              # タイトルバーに表示する文字
    font = pg.font.Font("./Lastkadai/ipaexg.ttf", 55) 
    screen.fill((137,189,222))                                    # 画面を空色に塗りつぶし
    text1 = font.render(str(point), True, (0,0,0)) #ボタンの文字を作成
    te_1=list(font.size(str(point)))
    button1 = pg.Rect((WIDTH-te_1[0])/2, 325, te_1[0], 60)        #ボタンもどきを生成
    text2 = font.render("Game Clear", True, (0,0,0)) #ボタンの文字を作成
    te_2=list(font.size("Game Clear"))
    button2 = pg.Rect((WIDTH-te_2[0])/2, 125, 310, 60)        #ボタンもどきを生成
    pg.mixer.music.load("./Lastkadai/fig2/勝利18.wav") 
    pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生
    
    while True:
        pg.draw.rect(screen, (206,155,14), button1)# 描画するボタンもどきの設定
        screen.blit(text1, ((WIDTH-te_1[0])/2, 325))          # 文字列の表示位置
        pg.draw.rect(screen, (255,255,0), button2)# 描画するボタンもどきの設定
        screen.blit(text2, ((WIDTH-te_2[0])/2, 125))          # 文字列の表示位置
        pg.display.update()     # 画面を更新
        # イベント処理
        for event in pg.event.get():
            if event.type == pg.QUIT:  # 閉じるボタンが押されたら終了
                return
            
def over_screen():#New
    WIDTH = 600
    HEIGHT = 500
    screen = pg.display.set_mode((WIDTH,HEIGHT))    # 大きさ600*500の画面を生成
    pg.display.set_caption("GAMEOVER")              # タイトルバーに表示する文字
    font = pg.font.Font("./Lastkadai/ipaexg.ttf", 55) 
    screen.fill((137,189,222))                                    # 画面を空色に塗りつぶし
    text1 = font.render("終了", True, (0,0,0)) #ボタンの文字を作成
    te_1=list(font.size("終了"))
    button1 = pg.Rect((WIDTH-te_1[0])/2, 325, 110, 60)        #ボタンもどきを生成
    text2 = font.render("Game Over", True, (0,0,0)) #ボタンの文字を作成
    te_2=list(font.size("Game Over"))
    button2 = pg.Rect((WIDTH-te_2[0])/2, 125, 290, 60)        #ボタンもどきを生成
    pg.mixer.music.load("./Lastkadai/fig2/zannense.mp3") 
    pg.mixer.music.play(loops=1, start=0.0)#ロードした音楽の再生
    while True:
        pg.draw.rect(screen, (40,52,85), button1)# 描画するボタンもどきの設定
        screen.blit(text1, ((WIDTH-te_1[0])/2, 325))          # 文字列の表示位置
        pg.draw.rect(screen, (148,87,164), button2)# 描画するボタンもどきの設定
        screen.blit(text2, ((WIDTH-te_2[0])/2, 125))          # 文字列の表示位置
        pg.display.update()     # 画面を更新
        # イベント処理
        for event in pg.event.get():
            msx,msy=pg.mouse.get_pos()#mouseのクリックを有無を取得
            msb=pg.mouse.get_pressed()#mouseの座標を取得
            if  msb ==(True,False,False) and msx>=240 and msx<= 350 and msy<=385 and msy>= 325:#終了ボタンが押されたなら
                return
            if event.type == pg.QUIT:  # 閉じるボタンが押されたら終了
                return

def music(num):#New
    if num=="1":
        if LEBEL_S=="EASY":
            pg.mixer.music.load("./Lastkadai/fig2/レッツゴー.mp3") 
            pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生
        if LEBEL_S=="NORMAL":
            pg.mixer.music.load("./Lastkadai/fig2/Inside-the-pyramid.mp3") 
            pg.mixer.music.play(loops=-1, start=0.0)#ロードした音楽の再生
        if LEBEL_S=="HARD":
            pg.mixer.music.load("./Lastkadai/fig2/Ys Healing  Dreams of the Goddess Feena.mp3") 
            pg.mixer.music.play(loops=-1, start=20.0)#ロードした音楽の再生
        if LEBEL_S=="Nightmare":
            pg.mixer.music.load("./Lastkadai/fig2/魔王魂 旧ゲーム音楽 ラストボス02.mp3") 
            pg.mixer.music.play(loops=-1, start=8.0)#ロードした音楽の再生
    elif num=="2":
        if LEBEL_S=="EASY":
            hit_1=pg.mixer.Sound("./Lastkadai/fig2/coin05.mp3")
            hit_1.play()
        if LEBEL_S=="NORMAL":
            hit_2=pg.mixer.Sound("./Lastkadai/fig2/audio_2329.wav")
            hit_2.play()
        if LEBEL_S=="HARD":
            hit_3=pg.mixer.Sound("./Lastkadai/fig2/crrect_answer2.mp3")
            hit_3.set_volume(0.2)
            hit_3.play()
        if LEBEL_S=="Nightmare":
            hit_4=pg.mixer.Sound("./Lastkadai/fig2/ショットガン発射.mp3")
            hit_4.play()

def music_sp():#New
    pg.mixer.music.stop()


if __name__ == "__main__":
    pg.init() # Pygameの初期化
    #clear_screen()
    #over_screen()
    start_screen()
    if START_GAME==True:
        NUM_H_BLOCK,NUM_V_BLOCK,WIDTH_BLOCK,HEIGHT_BLOCK,COLOR_BLOCK,HEIGHT_SPACE,WIDTH_PADDLE,HEIGHT_PADDLE,Y_PADDLE, COLOR_PADDLE,RADIUS_BALL,COLOR_BALL,NUM_BALL,BG_PG=level(LEBEL_S)
        pg.init()
        app = tk.Tk()
        app.title("ブロック崩し")
        Breakout(app)
        app.after(1000,count_up)
        app.mainloop()
    if CLEAR_GAME==True:
        clear_screen(SCORE)
    if OVER_GAME==True:
        over_screen()
    pg.quit()       # Pygameの終了(画面閉じられる)
