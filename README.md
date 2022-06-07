### ブロック崩し
- ゲーム概要C0B21164
    - 床をマウスで横に操作してボールを奈落に落とさずにブロックを破壊しよう。
    - ブロックを1つ破壊すると1ポイント、連続で破壊するとポイント+2*n|n=連続で破壊した数*(1~10の乱数)入るよ。
    - 難易度全部で三つ
    - キミは攻略できるかな？

- 仕様説明
    - 参考文献 |
        [ブロック崩しゲームの作り方](https://daeudaeu.com/tkinter-breakout/)
    
    - 主なクラス
        - Ball(100~273行)
            - ボールに必要な要素を作ったクラス
                - __init__ でボールの中心座標、半径、移動距離の設定
                - 残りの関数はボールの反射による対応(move, turn, reflectH, reflectV, getCollisionCoords, reflect関数)と画面ナインにあるか確認(exists関数)

        - Paddle(276~300)
            - パドルに必要な要素を作ったクラス
                - __init__ でパドルの中心座標、半径、移動距離の設定
                - move関数によるマウスの移動距離を記録

        - Block(303~317)
            - ブロックに必要な要素を作ったクラス
                - __init__ でパドルの中心座標、半径、移動距離の設定

        - (注釈)
            - 上の三つの中には、左上の座標と右下の座標の取得する「getCoords」がある。 

        - Breakout(321~780)
            - ブロック崩しゲームの全体を制御するクラス
                - __init__ で、背景(createWidgets関数)とボール, パドル, ブロック(createObjects、drawFigures関数)の描画とsetEvents関数によって、クリックするとゲームスタート(start関数), マウスカーソルの位置に応じてパドルを移動させること(motion関数)ができる関数を呼び出す

                - start関数に行くと、ゲーム開始していなかったら(self.is_playingがFalseの場合)loop関数にする。また、ゲームが開始してたら(self.is_playingがTrueの場合)止まる
                
                - loop関数に行くと、ボールの当たり判定ができ、当たったときのブロックの削除などの対応をするcollision関数、ボールとパドルの移動を描画するupdateFigures関数、ゲームクリアとゲームオーバーの時の実行を書いているresult関数をループして呼び出す
    - count_down関数は制限時間をカウントする 
    - C0B21166
    - score関数はブロック破壊時にポイントを加算する。床に戻らず連続で破壊したらボーナスポイントも加算される。
    - start_screen関数はスタート画面を作成および難易度設定の引数を返す
    - level関数は難易度設定の引数LEVEL_Sを用いて難易度に即した【パドルやボールのサイズ等】を返す。
    - clear_screen関数はゲームクリア時に実行する
    - over_screen関数はゲームオーバー時に実行する
    - music関数は各難易度に合わせたBGMとブロックを破壊した時の効果音を返す。
    - ゲームプレイ中に選択した難易度を左上に表示
    - C0B21004
    - 五秒間でボールの速さが１上がるように変更
    - C0B21044
    - 処理中にクリックされると"Pause"を表示
    - Breakoutクラスのcollision関数に消えたブロックの数によって、パドルの大きさを変えた
    - C0B21156

- 仕様BGM・画像
    - [BOOTH様](https://booth.pm/ja/items/10834)
    - [Freem 様](https://www.freem.ne.jp/)
    - [kamatamago.com様](https://kamatamago.com/sozai/bgm/B00096/)
    - [photo-ac様](https://www.photo-ac.com/main/detail/23505346)
    - [Pocket Sound様](https://pocket-se.info/archives/tag/%E3%82%B2%E3%83%BC%E3%83%A0%E3%82%AA%E3%83%BC%E3%83%90%E3%83%BC/)
    - [Senses Circuit様](https://www.senses-circuit.com/)
    - [Taira komori様](https://taira-komori.jpn.org/game01.html)
    - [ニコニコモンズ様](https://commons.nicovideo.jp/)
    - [フリー素材.com様](https://free-materials.com/%e7%a0%82%e4%b8%98%e3%83%bb%e7%a0%82%e6%bc%a013/)
