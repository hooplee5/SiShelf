# SiShelf [Var.1.1]

![SiShelf](/images/01.png)

Softimageのシェルフをリスペクトして作成されたMaya用のシェルフツールです。  
見た目のカスタマイズや自由な配置が行え、標準のシェルフツールよりも自分好みのシェルフを作成出来ます。  
また、Mayaメインウインドウにドッキングした状態だけでなく、フローティングウインドウとしても利用できます。  

## バージョン1.0から1.1への移行手順

初期型のバージョン1.0では手動でuserSetup.pyにコードを記述していましたが、1.1からは指定の場所にフォルダを置くだけで良くなりました。
1.0を導入した方は以下の手順で1.1へと移行してください。  

1. SiShelf[Var.1.0]フォルダの直下にあるdataフォルダを `C:\Users\ユーザー名\Documents\maya` へ `SiShelf_data` とリネームして移動させる。
2. userSetup.pyに追記した部分を削除。
3. 下記インストール項目の手順でVar.1.1をインストール

## インストール

ダウロードしたSiShelfフォルダを `C:\Program Files\Autodesk\ApplicationPlugins` へコピーしてください。

 ※複数バージョンのMayaに対応しています。2014以降のバージョンでは自動的に認識されツールが使える状態になります。

 ※不要になった場合はフォルダを削除してください。

## 実行

メインメニュー > Windows > SiShelf から開くことが可能です。もしくは Hotkey Editor > Custom Scripts > SiShelf からホットキーを割り振ることもできます。  

![SiShelf](/images/09.png)

コードから実行する場合は以下の通りです。（上記コードをスクリプトエディタ(Pythonタブ)に貼り付けて実行 ）

+ ウインドウが画面中央に表示されます。
```python
   import SiShelf.shelf
   SiShelf.shelf.main()
```

+ マウスの位置にポップアップ
```python
   import SiShelf.shelf  
   SiShelf.shelf.popup()  
```


## 使い方

### Mayaウインドウへのドッキング

SiShelfはMayaのウインドウにドッキングすることができます。  
ドッキングした状態でMayaを終了すると状態が保存され、次回ドッキングした状態でMayaが起動します。  

![SiShelf](/images/04.png)

### ボタンの登録

シェルフにツールを登録する方法は以下の２つです。

+ テキストを選択してシェルフにドラッグ＆ドロップ
+ ファイルをシェルフにドラッグ＆ドロップ（.melファイル、.pyファイルに対応）

![SiShelf](/images/02.png)

ボタンの設定ウインドウが表示されるので任意の情報を入力してOKを押すとボタンが作成されます。 

![SiShelf](/images/03.gif)
  
マウスの左クリックでスクリプトを実行できます。


### 仕切り線

タブ内の整理用に仕切り線を追加できます。
縦横やラベルの有無、色などが自由に設定できます。

![SiShelf](/images/05.gif)


### タブ

マウス右クリックのコンテキストメニューからタブの追加、削除、リネームが行えます。  
タブの順番はドラッグすることで入れ替えることが可能です。  

![SiShelf](/images/06.gif)

### 操作

パーツはマウス中ドラッグで配置移動を行うことができます。

![SiShelf](/images/07.gif)

マウスの左ドラッグでシェルフに登録したパーツを矩形選択できます。
複数選択した状態でマウス中ボタンドラッグで一括移動、コンテキストメニューから削除等が出来ます。  
※現状複数選択に対応していないコマンドもあります。

![SiShelf](/images/08.gif)

### コンテキストメニュー

マウス右クリックでコンテキストメニューを表示できます。

+ Add button  
　→ ボタンを追加します。
+ Add partition  
　→ 仕切り線を追加します。
+ Edit  
　→ 選択しているパーツの内容を編集します。（複数選択には対応していません。）
+ Delete  
　→ 選択しているパーツを削除します。
+ Copy  
　→ 選択しているパーツをコピーします。（複数選択には対応していません。）
+ Paste  
　→ コピーしたパーツをクリックした位置に貼り付けます。
+ Cut  
　→ 選択しているパーツを切り取ります。（複数選択には対応していません。）
+ Tab > Add  
　→ タブを追加します。
+ Tab > Rename  
　→ 現在のタブの名前を変更します。
+ Tab > Delete  
　→ 現在のタブを削除します。タブを削除するとタブに配置していたパーツ情報もすべて削除されます。
+ Default setting > Button  
　→ ボタンを作る際の初期設定を行います。
+ Default setting > Partition  
　→ 仕切り線を作る際の初期設定を行います。

### データの保存

シェルフ内のデータはパーツの追加、削除、移動などの操作を行ったタイミングで自動的に保存されます。  
現状は元に戻す機能はありません。注意してください。  

データは `C:\Users\ユーザー名\Documents\maya` にjsonファイルとして作成れます。  
jsonファイルはテキストファイルなので、やろうと思えば内容を変更して保存することで手動での書き換えも可能です。  
複数バージョンのMayaからも同一データが参照されます。現状はバージョン違いによる参照先変更機能はありません。


## 動作確認

MAYA2014：ドッキング等は出来ないが立ち上がると思う（未確認）

MAYA2015：問題なし

MAYA2016：問題なし

MAYA2017：一部不具合有


### 把握している不具合

+ windows10でボタン名に2バイト文字を入力するとMayaが落ちる現象
+ MAYA2017でドッキング状態でMAYAを終了しても再起動の際復元されない。


## 改訂履歴


2017/4/13
+ バージョン1.1.1公開
+ 不要なPYTHONPATHの設定を削除。内部のインポートを明示的相対インポートに変更
+ タブ内のパーツをEditした際に古いデータが残ってしまっていたバグを修正

2017/4/12
+ バージョン1.1公開
+ PackageContents.xml形式に対応。
+ メニューとホットキーエディタに情報を自動登録対応
+ ボタンエディット後に背景色の適用が正常に行えていなかったのを修正
+ ボタンエディット画面のプレビュー時に背景色が反映されていなかったバグを修正
+ MAYA2017でシェルフへファイル投げ込みを行うとエラーになっていた問題を解消
+ その他細かいMAYA2017用の対応

2017/4/10  
+ Maya2016でボタンの背景色指定が無効になっていたバグを修正
+ 「準備」の項目にgithubからzipをダウンロードした際の注記を追加

2017/4/9  
+ バージョン1.0公開


## ライセンス

[MIT](https://github.com/mochio326/SiShelf/blob/master/LICENSE)
