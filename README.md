### ブロック崩し
- ゲーム概要
    - 床をマウスで横に操作してボールを奈落に落とさずにブロックを破壊しよう。
    - ブロックを1つ破壊すると1ポイント、連続で破壊するとポイント+2*n|n=連続で破壊した数*(1~10の乱数)入るよ。
    - 難易度全部で三つ
    - キミは攻略できるかな？

- 仕様説明
    - 参考文献 |
        [ブロック崩しゲームの作り方](https://daeudaeu.com/tkinter-breakout/)
    - 画面サイズ【1000*700】
    - Ballクラスではボールの作成と移動情報【加速度や進行方向など】
    - Paddleクラスでは移動床の座標を取得する。
    - Blockクラスはブロックの図形サイズを決定する。
    - Breakoutクラスはゲームを動作させる。
    - count_up関数は経過時間をカウントする
    - score関数はブロック破壊時にポイントを加算する。床に戻らず連続で破壊したらボーナスポイントも加算される。
    - start_screen関数はスタート画面を作成および難易度設定の引数を返す
    - level関数は難易度設定の引数LEVEL_Sを用いて難易度に即した【パドルやボールのサイズ等】を返す。
    - clear_screen関数はゲームクリア時に実行する
    - over_screen関数はゲームオーバー時に実行する
    - music関数は各難易度に合わせたBGMとブロックを破壊した時の効果音を返す。

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