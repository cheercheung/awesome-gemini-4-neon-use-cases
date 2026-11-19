<div align="center">

<a href="https://evolink.ai/gemini-4-neon?utm_source=github&amp;utm_medium=banner&amp;utm_campaign=awesome-gemini-4-neon-use-cases&amp;utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/banner/neon-use-cases-b56d48e57ac3.png" alt="Gemini 4 Neon Use Cases" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

<a id="introduction"></a>
## 🍌 はじめに

**公開ワークフロー、ビジュアル プロトタイプ、統合、評価を通じて Gemini 4 Neon を探索します。各ケースはソースにリンクし、モデルの役割と報告された結果を説明します。**

<a id="overview"></a>
## 📊 概要

**Gemini 4 Neon の事例 95 件**と、出典に基づく 124 点のビジュアルを掲載しています。

- エンジニアリングと統合 · 6
- グラフィックスとインターフェイスのプロトタイプ · 51
- ゲームとシミュレーション · 12
- 知識労働 · 8
- 評価と限界 · 18

> [!NOTE]
> 各事例には出典へのリンクがあります。所要時間、費用、ベンチマークの結果は、記載された条件での観測値です。

<a id="quick-start"></a>
## ⚡ クイックスタート

1. メニューからケースを選択し、その元のソースを開きます。
2. ソースが報告するモデルの役割、ツール、設定、結果を確認します。
3. タスクと設定が一致するケースを比較します。作成者が報告した時間とコストは、それらの実行からの観察として扱います。

<a id="menu"></a>
## 📑 メニュー

| ケース | カテゴリ | それが示すもの | タイプ |
|---|---|---|---|
| [無人実行中の不安定性を観察する](#case-1) | エンジニアリングと統合 | 検証者は、リリース当日に Neon を画面のない環境で動かすと不安定だったと報告しています。実行は Opus 5.5 が監視していたとのことです。 | Limit |
| [論理ゲートのシミュレーションを作る](#case-2) | エンジニアリングと統合 | 著者は、シミュレートされた論理ゲートや回路基板からレトロな端末ディスプレイに至るまで、インタラクティブなエレクトロニクスのデモを示しています。 | Demo |
| [tscircuit で Bluetooth 歯ブラシを設計する](#case-3) | エンジニアリングと統合 | tscircuit の管理者が、Bluetooth 電動歯ブラシで Neon High、Opus 5.5 High、および Sol 6.2 High を比較しました。 | Evaluation |
| [Muse のサイドカンバセーションを Neon に中継します](#case-4) | エンジニアリングと統合 | 著者は、リクエストと返信を Neon に渡す Muse サイド チャットを構築しました。 | Integration |
| [3 つのモデルを使用した T3 Code ワークフローでのコピーライティングに Neon を使用する](#case-5) | エンジニアリングと統合 | 開発者は、Neon に、マルチモデル T3 Code ワークフロー内でコピーライティングの役割を与えます。 | Integration |
| [Spotify のおすすめ MCP を作り直す](#case-6) | エンジニアリングと統合 | 作成者は Neon を使用して、もともと Argon で構築された Spotify レコメンデーション MCP を改訂しました。 | Integration |
| [車の SVG 側面図を描画する](#case-7) | グラフィックスとインターフェイスのプロトタイプ | 作成者は AI Studio の Neon high を使用して、BMW M4 CS のサイドビュー SVG を作成しました。 | Demo |
| [SVG テスト シリーズを実行する](#case-8) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Neon SVG テスト シリーズの 3 つの出力を共有しました。 | Demo |
| [Three.js でペリカンをアニメーション化する](#case-9) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Three.js の自転車に乗ったペリカンの出力が Neon によるものであると考えています。 | Demo |
| [xhigh で SVG ポートレートを描画する](#case-10) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Neon xhigh によるアナ デ アルマスの肖像画を共有しています。 | Demo |
| [中程度の労力でサイクリング ペリカンをアニメーション化する](#case-11) | グラフィックスとインターフェイスのプロトタイプ | 著者は Neon を中程度の労力で使用してペリカンのサイクリング デモを作成し、ビデオを投稿しました。 | Demo |
| [2 つのボクセル ガーデン シーンを比較する](#case-12) | グラフィックスとインターフェイスのプロトタイプ | 著者は、Neon xhigh のボクセル ガーデンを GPT-6.2 Sol xhigh の結果とともに投稿しました。 | Evaluation |
| [Three.js および GLSL シーンを生成する](#case-13) | グラフィックスとインターフェイスのプロトタイプ | 作成者は Neon からの Three.js と GLSL の出力を共有し、2 分 40 秒の実行を報告しています。 | Demo |
| [完全にコードで絵画を作成する](#case-14) | グラフィックスとインターフェイスのプロトタイプ | 作成者は、早期アクセスの Neon を使用して絵画をレンダリングするコードを作成したと報告しています。 | Demo |
| [ペリカンのサイクリングアニメーションを比較する](#case-15) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Neon、Hydrogen、GPT-6.2 Astra、GPT-6.2 Sol のペリカン アニメーションを比較しました。 | Evaluation |
| [Three.js サイクリング アニメーションを 3 つのモデル間で比較](#case-16) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Neon、Opus 5.5、および Carbon の Three.js サイクリング比較を公開しました。 | Evaluation |
| [海上の背の高い船をレンダリングします。](#case-17) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Neon xhigh による海洋セーリング シーンを共有しました。 | Demo |
| [ボクセル パゴダを生成する](#case-18) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Neon xhigh で生成されたボクセル パゴダを投稿します。 | Demo |
| [自転車に乗ってイライラするペリカンを描く](#case-19) | グラフィックスとインターフェイスのプロトタイプ | 作成者は AI Studio の Neon high を使用して、自転車に乗ってイライラするペリカンの SVG を描画しました。 | Demo |
| [ゲームパッドの描画を GPT-6.2 Sol と比較](#case-20) | グラフィックスとインターフェイスのプロトタイプ | テスターは、各モデルの利用可能な最高の推論で同じプロンプトを使用し、出力が類似していると判断しました。 | Evaluation |
| [3D 水上飛行機を生成する](#case-21) | グラフィックスとインターフェイスのプロトタイプ | テスターは Neon xhigh を使用して 3D 水上飛行機を構築し、ビデオを共有しました。 | Demo |
| [2D の馬を描く](#case-22) | グラフィックスとインターフェイスのプロトタイプ | 作者はNeonを使って二次元の馬を制作し、その出力物を投稿しました。 | Demo |
| [雨のコンビニシーンをテストしてみる](#case-23) | グラフィックスとインターフェイスのプロトタイプ | テスターは Neon と GPT-6.2 Sol に対して同じプロンプトを使用し、比較を投稿しました。 | Evaluation |
| [1 つの画像から四足歩行のロボットをアニメーション化する](#case-24) | グラフィックスとインターフェイスのプロトタイプ | 開発者は Neon に 1 つの参考画像を与え、3D モデルを要求しました。 | Demo |
| [バニラ JavaScript で Keats をアニメーション化する](#case-25) | グラフィックスとインターフェイスのプロトタイプ | Google チームのメンバーは、Keats の To Autumn のバニラ JavaScript アニメーションについては、GeokenAI と Neon の功績を認めています。 | Demo |
| [トリケラトプスのデモを作成する](#case-26) | グラフィックスとインターフェイスのプロトタイプ | 作成者は、トリケラトプスのデモンストレーションは Neon によるものだと考えています。 | Demo |
| [3D 歯車列レンダリングを比較する](#case-27) | グラフィックスとインターフェイスのプロトタイプ | テスターは、ラベル付き推論レベル全体で Neon、Carbon、Astra、Sol の歯車機構のレンダリングを表示します。 | Evaluation |
| [1 つの HTML ファイルで 10 個のインタラクティブなエフェクトを作成する](#case-28) | グラフィックスとインターフェイスのプロトタイプ | Google チームのメンバーは、Neon を使用して 1 つの 27 KB HTML ファイルに 10 個のインタラクティブ 3D 効果を作成したと報告しています。 | Demo |
| [Antigravity Swarm を使用して Blender ラボベンチを構築する](#case-29) | グラフィックスとインターフェイスのプロトタイプ | Google は、Antigravity Swarm と Blender を使用して Gemini 4 ファミリーをテーマにした実験台のシーンを作成する Neon をデモンストレーションしました。 | Integration |
| [建築イラストと Opus 5.5 を比較する](#case-30) | グラフィックスとインターフェイスのプロトタイプ | テスターは、同じプロンプトを使用して、可能な限り最高の推論を使用してモデルを比較しました。 | Evaluation |
| [ボイジャー1号の飛行を可視化する](#case-31) | グラフィックスとインターフェイスのプロトタイプ | 著者は、打ち上げから木星との遭遇までのボイジャー 1 号の 3D シーケンスと探査機のクローズアップを示しています。 | Demo |
| [3Dプラネタリウムを作る](#case-32) | グラフィックスとインターフェイスのプロトタイプ | 著者は、惑星間を移動する 3D プラネタリウムと星座ビューを示しています。 | Demo |
| [バベッジの階差機関第2号を可視化する](#case-33) | グラフィックスとインターフェイスのプロトタイプ | 著者は、ギア アセンブリと数値表示を備えたバベッジのディファレンス エンジン No. 2 の 3D 視覚化を示しています。 | Demo |
| [アンティキティラ島の機械を可視化する](#case-34) | グラフィックスとインターフェイスのプロトタイプ | 著者は、回収された物体、復元された歯車、ダイヤルを切り替える 3D アンティキティラ メカニズムのデモを示しています。 | Demo |
| [気流を可視化する風洞の試作を作る](#case-35) | グラフィックスとインターフェイスのプロトタイプ | 著者は、さまざまな形状の周りに目に見える空気の流れの流線を備えた 3D 風洞デモを示しています。 | Demo |
| [キングス・カレッジ礼拝堂の断面を再現する](#case-36) | グラフィックスとインターフェイスのプロトタイプ | 著者は、外部と内部が切り替わるキングス カレッジ礼拝堂の 3D 断面図を示しています。 | Demo |
| [川に架かる高架橋と周辺を描画する](#case-37) | グラフィックスとインターフェイスのプロトタイプ | 著者は、マルチアーチ高架橋、列車、およびいくつかのレンダリング ビューを備えた 3D の川の渓谷を示しています。 | Demo |
| [ケンブリッジを思わせる3Dの街並みを作る](#case-38) | グラフィックスとインターフェイスのプロトタイプ | 著者は、ケンブリッジにインスピレーションを得た都市のビジュアライゼーションを、モデル化された街区の上空からの眺めとより近い視点で示しています。 | Demo |
| [ネオンをテーマにした地球をレンダリングする](#case-39) | グラフィックスとインターフェイスのプロトタイプ | 作者は Antigravity で Neon の High 設定を使い、ネオンをテーマにした地球をレンダリングしました。 | Demo |
| [ヨットのシーンを反復する](#case-40) | グラフィックスとインターフェイスのプロトタイプ | 作成者は、Neon がヨット シーンを改善したと報告し、その出力を示しています。 | Demo |
| [カスタム VFX ツールで衣装素材を作成する](#case-41) | グラフィックスとインターフェイスのプロトタイプ | 作者は Neon を使って衣装素材を作成し、その結果の画像 6 枚を投稿しました。 | Demo |
| [ボクセルNinjagoシーンの比較](#case-42) | グラフィックスとインターフェイスのプロトタイプ | ソースでは、ボクセル再現で Neon と Fable 5.2 を比較しています。 | Evaluation |
| [ペリカン製品のモーショングラフィックを作成する](#case-43) | グラフィックスとインターフェイスのプロトタイプ | 制作者は、ペリカンをテーマにした製品のモーション グラフィックを Neon に提供したと認めています。 | Demo |
| [ニューヨーク市のシーンのプロトタイプを比較する](#case-44) | グラフィックスとインターフェイスのプロトタイプ | テスターの報告によると、Neon にはブルックリン橋、自由の女神、タクシーが通る通りが含まれていました。 | Evaluation |
| [バナナのビジュアルテストを実行する](#case-45) | グラフィックスとインターフェイスのプロトタイプ | テスターは、Banana Test というタイトルのテストの Neon 出力を投稿します。 | Demo |
| [幽霊が出る大聖堂を 1 つのプロンプトで比較する](#case-46) | グラフィックスとインターフェイスのプロトタイプ | テスターは Neon と GPT-6.2 Sol に同じ幽霊の大聖堂のタスクを与えました。 | Evaluation |
| [Antigravity で電話アセンブリのプロトタイプを作成する](#case-47) | グラフィックスとインターフェイスのプロトタイプ | 開発者は Antigravity で Neon を使用し、設計コンポーネントのボードとレンダリングされた電話アセンブリを示しました。 | Demo |
| [インタラクティブな歴史的帆船を生成する](#case-48) | グラフィックスとインターフェイスのプロトタイプ | 著者はゼロショット 3D 帆船のデモンストレーションを投稿しました。 | Demo |
| [JavaScript でモデル導入を設計する](#case-49) | グラフィックスとインターフェイスのプロトタイプ | 著者は Neon を使用してモデルを紹介するモーション グラフィックを作成しました。 | Demo |
| [スキー小屋のシーンを 1 つのパスで生成する](#case-50) | グラフィックスとインターフェイスのプロトタイプ | DesignArena は、Neon と Argon に同じアルプス小屋の設定を生成するよう依頼し、並べて出力したものを公開しました。 | Evaluation |
| [ボクセルのファンタジー城をレンダリングする](#case-51) | グラフィックスとインターフェイスのプロトタイプ | 作成者は、Neon xhigh で作成されたボクセル城を共有しています。 | Demo |
| [タコのサイクリングアニメーションをAstraと比較してください](#case-52) | グラフィックスとインターフェイスのプロトタイプ | 検証者の記録では、Astra (xhigh) は 21 分 53 秒で 2.52 米ドル、Neon (high) は 41 分で 4.02 米ドルでした。 | Evaluation |
| [Three.js 蝶のアニメーション](#case-53) | グラフィックスとインターフェイスのプロトタイプ | クリエイターは Antigravity の Neon xhigh を使用して Three.js の蝶のアニメーションを作成しました。 | Demo |
| [参照画像からコンポーネントとモーションを構築する](#case-54) | グラフィックスとインターフェイスのプロトタイプ | 作成者は視覚的な参照を使用して、いくつかのコンポーネントとそれに伴うモーションを生成しました。 | Demo |
| [Three.js のピクセル ウィザードの世界](#case-55) | グラフィックスとインターフェイスのプロトタイプ | 作成者は Neon の参考画像を提供し、3 回のパスにわたって Three.js シーンを改良しました。 | Demo |
| [城のレンダリングベンチマーク](#case-56) | グラフィックスとインターフェイスのプロトタイプ | 作者は Neon を城のベンチマークに使用し、動画と静止画を投稿しました。 | Evaluation |
| [アラン・チューリングの1936年当時の書斎を再現する](#case-57) | グラフィックスとインターフェイスのプロトタイプ | Google は、Neon と Antigravity Swarm を使用して、アーカイブ写真からインタラクティブな再構成を構築しました。 | Demo |
| [横スクロール障害物ゲームを構築する](#case-58) | ゲームとシミュレーション | テスターは Neon に Flappy Bird スタイルのプロトタイプを依頼し、その録音を投稿しました。 | Demo |
| [剣と盾の戦闘シーンを比較](#case-59) | ゲームとシミュレーション | テスターは、戦闘ゲーム シーンの Fable 5.2 および Neon 出力のラベルが付いたビデオを投稿しました。 | Evaluation |
| [シンセウェーブ風のミニゴルフゲームを作る](#case-60) | ゲームとシミュレーション | Google Antigravity は、Gemini 4 Neon が Swarm を使い、1 つのプロンプトから 3D ミニゴルフゲームを作る様子を公開した。 | Demo |
| [アニメの騎士の決闘を比較する](#case-61) | ゲームとシミュレーション | テスターは、装甲キャラクター間の決闘用に、ラベル付きの Opus 5.5 と Neon の出力を別々に投稿しました。 | Evaluation |
| [1 つの HTML ファイルで表現主義アート ゲームを作成する](#case-62) | ゲームとシミュレーション | 開発者は Neon を使用して、1 つの HTML ファイルに含まれるエンドレスの JavaScript アート ゲームを作成しました。 | Demo |
| [アイスボス ゲームのプロトタイプを比較する](#case-63) | ゲームとシミュレーション | テスターは、一人称アイスボスとの遭遇用に、ラベル付きの Neon および Opus 5.5 出力を投稿しました。 | Evaluation |
| [スイカバスケットボールのデモ](#case-64) | ゲームとシミュレーション | テスターは Neon スイカ バスケットボールのビデオを共有しています。 | Demo |
| [ガウス スプラッティング ベーカリー プラットフォーマーを構築する](#case-65) | ゲームとシミュレーション | 作成者は Neon を使用して、C++20 と WebGPU のガウス スプラッティング エンジンを 4 タワー プラットフォーマーに変えました。 | Demo |
| [Antigravity Swarm で 3D ゲームを構築する](#case-66) | ゲームとシミュレーション | 開発者は Neon と Antigravity Swarm を使用して小さな 3D ゲームを構築しました。 | Demo |
| [宇宙レーシングプロトタイプ](#case-67) | ゲームとシミュレーション | クリエイターは、Neon を使用してスペース レーサーを高い推論で構築したと報告しました。 | Demo |
| [タワーディフェンスのプロトタイプ](#case-68) | ゲームとシミュレーション | 開発者は、Neon で構築されたタワーディフェンス プロトタイプのゲームプレイを投稿しました。 | Demo |
| [一人称視点のスキー シミュレーターを構築する](#case-69) | ゲームとシミュレーション | Google は、Neon を使用してモンブランとシャモニーの地形で WebGL2 フリーライド シミュレーターを作成したと報告しています。 | Demo |
| [モデルの選択を調査表に要約する](#case-70) | 知識労働 | 著者は、Gemini 4 モデル選択テーブルは Neon によって実行された研究によるものであると考えています。 | Demo |
| [Neon とローンチ フィルムを共同作成する](#case-71) | 知識労働 | Google チームのメンバーが Neon と映画を共同制作したことを報告し、その結果を共有します。 | Demo |
| [VR ゲームの機器の仕組みを説明する](#case-72) | 知識労働 | 筆者はメタクエストゲームH3VR2の装備をNeonを使ってまとめ、図解付きの解説をつけました。 | Demo |
| [画像のトリミング中に自己評価を検査する](#case-73) | 知識労働 | テスターは、画像編集テスト中に Neon が自身の作物を補完したと報告しました。 | Limit |
| [記事を編集可能なスライドに変換する](#case-74) | 知識労働 | 作成者は Neon に記事を送信し、公開スライド作成スキルを使用しました。 | Demo |
| [ファンタジー小説のオープニングを生成する](#case-75) | 知識労働 | 著者は、Neon をライティング テストに使用し、中国のファンタジー物語の冒頭を公開しました。 | Demo |
| [オリジナルのダリオジョークを解釈する](#case-76) | 知識労働 | 著者は、Neon は自分たちが書いたジョークを理解したが、Opus 5.5 は理解できなかったと報告しています。 | Evaluation |
| [スプレッドシートでコンピューター ビジョン ラボを構築する](#case-77) | 知識労働 | Google は、Neon の群れが 1 つの参照画像を 100,000 セルのスプレッドシートに変えたと報告しています。 | Demo |
| [Vals Index でドメインのパフォーマンスを測定する](#case-78) | 評価と限界 | Vals AI は、Neon で 70.9% を報告し、Fable 5.2 に 0.4 ポイント差の 2 位の総合順位を記録しました。 | Benchmark |
| [早期アクセス中にインタラクティブなデモをテストする](#case-79) | 評価と限界 | 著者は、Antigravity で Neon を使用して 17 のインタラクティブなデモを構築し、追加のコーディングとツールのテストを文書化したと報告しています。 | Evaluation |
| [Agent Arena でエージェント セッションを比較する](#case-80) | 評価と限界 | Arena の報告では Neon High は 1336 ポイントで 2 位、タスクあたりの費用の中央値は 2.82 米ドルでした。 | Benchmark |
| [Neon を Text Arena に配置](#case-81) | 評価と限界 | Arena の発表では、Neon High は 1518、Carbon High は 1526、Argon High は 1521 でした。 | Benchmark |
| [Wojak-Benchで3Dプリント用のフィギュアを評価する](#case-82) | 評価と限界 | ベンチマークの共著者は、Neon が 4 位でデビューしたと報告しました。投稿されたリーダーボードのスナップショットでは、Neon の評価は 1056 です。 | Benchmark |
| [コーディング エージェントとそのハーネスを比較する](#case-83) | 評価と限界 | 人工分析では、Antigravity CLI を使用した Neon xhigh については 59、Carbon high については 55 が報告されます。 | Benchmark |
| [AA-Briefcase でのナレッジ ワークを評価する](#case-84) | 評価と限界 | 人工分析では、Neon xhigh の Elo が 1700、Carbon high の Elo が 1611 と報告されています。 | Benchmark |
| [Artificial Analysis Intelligence Index タスクの時間を計測する](#case-85) | 評価と限界 | Artificial Analysis の報告では、1 タスクあたりの所要時間は Neon xhigh が約 21 分、Carbon high が約 36 分でした。 | Benchmark |
| [自動販売機ビジネスのシミュレーションを実行する](#case-86) | 評価と限界 | Andon Labs は、投稿時に Vending-Bench 2 で Neon を最初に報告しました。 | Benchmark |
| [RuneScape ベンチマークの制限時間を調べる](#case-87) | 評価と限界 | ベンチマーク作成者は、Neon の野心的な戦略が期限までに完了しなかったと報告しました。 | Limit |
| [APEX-Agents で専門的なタスクを実行する](#case-88) | 評価と限界 | Mercor は、APEX-Agents の Neon の Pass@1 スコアが 82.9%、平均スコアが 88.9% であると報告しています。 | Benchmark |
| [CursorBench 4.1 での Neon と Hydrogen の比較](#case-89) | 評価と限界 | Cursor は、デフォルトの努力で Neon について 63.7%、Hydrogen について 57.3% を報告します。 | Benchmark |
| [CUDA デバッグ タスクの実時間を測定する](#case-90) | 評価と限界 | 著者は CUDA デバッグ プロンプトでモデルを実行し、トークン レートとエンドツーエンドの遅延を個別に測定しました。 | Benchmark |
| [Tuesday@Work で職場のタスクを測定する](#case-91) | 評価と限界 | Surge AI は評価スイートで Neon を実行し、Tuesday@Work では 71.6 を報告しましたが、Fable 5.2 では 71.2 でした。 | Benchmark |
| [Antigravity でのペナルティ決定を確認する](#case-92) | 評価と限界 | Penalty Bench の作成者は、Neon が Antigravity ハーネスを使用したベンチマークで 1 位にランクされたと報告しています。 | Benchmark |
| [ブラウザ使用ベンチマーク](#case-93) | 評価と限界 | Browser Use では、Neon の結果が 74% で、Opus 5.5 の結果と同等、GPT-6.2 Sol の 82% と報告されました。 | Benchmark |
| [PandaCode でのツール呼び出しの失敗を測定する](#case-94) | 評価と限界 | 著者は、1 回の起動夜のウィンドウで、9,465 回の Neon 呼び出しのうち、65 回の失敗したツール呼び出しを測定しました。 | Evaluation |
| [43 の質問からなる Plotly データ分析ベンチマークを実行する](#case-95) | 評価と限界 | Plotly の修正結果では、Neon が 43 件中 43 件の回答を獲得し、フル実行で 17.03 米ドルと報告されています。 | Benchmark |

| セクション | 目的 |
|---|---|
| [関連リポジトリ](#related-repositories) | その他のジェミニのケースコレクション |
| [クイックスタート](#quick-start) | 事例の読み方 |
| [謝辞](#acknowledge) | クレジットと修正 |

## 🛠️ エンジニアリングと統合
<a id="engineering"></a>

<a id="case-1"></a>
### Case 1: [無人実行中の不安定性を観察する](https://x.com/IndependentEco/status/2123155946801070204) (by [@IndependentEco](https://x.com/IndependentEco))

**無人実行での再試行と完了を追跡し、監視モデルの別の記録を保持します。**

検証者は、リリース当日に Neon を画面のない環境で動かすと不安定だったと報告しています。実行は Opus 5.5 が監視していたとのことです。

スクリーンショットはその環境を記録しています。この報告書は根本原因を特定していません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-1-1-cffe1f4d2f8c.png" alt="無人実行中の不安定性を観察する · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-1-2-33b7cb88e773.png" alt="無人実行中の不安定性を観察する · 2" width="560">

Type: Limit | Date: 2026-11-18

---

<a id="case-2"></a>
### Case 2: [論理ゲートのシミュレーションを作る](https://x.com/SamuelAlbanie/status/2123174394889687151) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**シミュレーションがチップ、回路基板、ディスプレイのレベルで何を示しているかを確認してください。**

著者は、シミュレートされた論理ゲートや回路基板からレトロな端末ディスプレイに至るまで、インタラクティブなエレクトロニクスのデモを示しています。

このシリーズでは、調整を行わずに、デモごとに 1 つのプロンプトをレポートします。記録には、インターフェイスとシミュレーションの動作が示されています。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-2-1-b7233891bf19.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-2-1-7cb8c5a2b86d.jpg" alt="論理ゲートのシミュレーションを作る · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-3"></a>
### Case 3: [tscircuit で Bluetooth 歯ブラシを設計する](https://x.com/seveibar/status/2123229845274653112) (by [@seveibar](https://x.com/seveibar))

**レンダリングされたエンクロージャとは別に、ルーティングとフットプリントの選択を確認します。**

tscircuit の管理者が、Bluetooth 電動歯ブラシで Neon High、Opus 5.5 High、および Sol 6.2 High を比較しました。

メンテナは Neon の視覚的な結果を好みましたが、不完全なルーティングと不適切なフットプリントの選択を報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-3-1-f5a7948ce417.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-3-1-c5c60f2fdcf3.jpg" alt="tscircuit で Bluetooth 歯ブラシを設計する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-4"></a>
### Case 4: [Muse のサイドカンバセーションを Neon に中継します](https://x.com/kajikent/status/2123232182298976767) (by [@kajikent](https://x.com/kajikent))

**Muse リレーに依存する前に、どの応答が Neon から来るかを確認してください。**

著者は、リクエストと返信を Neon に渡す Muse サイド チャットを構築しました。

掲載されている日本語説明書はMuseリレーを設定します。これは Muse への指示であり、Neon に送信される直接のプロンプトを確立するものではありません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-4-1-7b5f3b451dc2.jpg" alt="Muse のサイドカンバセーションを Neon に中継します · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-4-2-636fe982bfee.jpg" alt="Muse のサイドカンバセーションを Neon に中継します · 2" width="560">

Type: Integration | Date: 2026-11-19

---

<a id="case-5"></a>
### Case 5: [3 つのモデルを使用した T3 Code ワークフローでのコピーライティングに Neon を使用する](https://x.com/theo/status/2123273253850628260) (by [@theo](https://x.com/theo))

**1 つのモデルをコピーライティングに割り当て、実装とプレイテストへの受け渡しを確認します。**

開発者は、Neon に、マルチモデル T3 Code ワークフロー内でコピーライティングの役割を与えます。

開発者は実装を Fable に割り当て、プレイテストを GPT-6.2 Astra に割り当てます。 T3 Code のスクリーンショットは、アクティブなワークフローでコピーライターが参加するクリーチャー育成ゲームを示しています。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-5-1-3899936a871e.jpg" alt="3 つのモデルを使用した T3 Code ワークフローでのコピーライティングに Neon を使用する · 1" width="560">

Type: Integration | Date: 2026-11-19

---

<a id="case-6"></a>
### Case 6: [Spotify のおすすめ MCP を作り直す](https://x.com/Lentils80/status/2123285929649455409) (by [@Lentils80](https://x.com/Lentils80))

**推奨事項の変更を確認し、要求されていない機能によって結果が改善されるかどうかをテストします。**

作成者は Neon を使用して、もともと Argon で構築された Spotify レコメンデーション MCP を改訂しました。

作成者は、バグ修正と、要求されていない嗜好ベースの推奨モデルを報告しました。この投稿は推奨の正確性を提供するものではありません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-6-1-a5dafa9b6b4e.jpg" alt="Spotify のおすすめ MCP を作り直す · 1" width="560">

Type: Integration | Date: 2026-11-19

---

## 🎨 グラフィックスとインターフェイスのプロトタイプ
<a id="graphics"></a>

<a id="case-7"></a>
### Case 7: [車の SVG 側面図を描画する](https://x.com/HarshithLucky3/status/2123158145380085991) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**コードレンダリングされた側面図を比較するときは、プロポーションとシルエットを確認してください。**

作成者は AI Studio の Neon high を使用して、BMW M4 CS のサイドビュー SVG を作成しました。

アーティファクトはポストに添付されます。完全なプロンプトは引用されていません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-7-1-ffea70bbfd83.png" alt="車の SVG 側面図を描画する · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-8"></a>
### Case 8: [SVG テスト シリーズを実行する](https://x.com/AdamHoltererer/status/2123159230291054903) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**SVG タスク間の一貫性を判断する前に、いくつかの出力を確認してください。**

テスターは、Neon SVG テスト シリーズの 3 つの出力を共有しました。

結果はまとめて表示され、1 つのテスト シリーズとしてカウントされます。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-8-1-2eb686ec5f13.jpg" alt="SVG テスト シリーズを実行する · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-8-2-7f4fbb41bac4.jpg" alt="SVG テスト シリーズを実行する · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-8-3-8ffa94a0957b.jpg" alt="SVG テスト シリーズを実行する · 3" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-9"></a>
### Case 9: [Three.js でペリカンをアニメーション化する](https://x.com/StatsWire/status/2123160089854898346) (by [@StatsWire](https://x.com/StatsWire))

**サイクリング モーションとシーン レンダリングをアニメーションの別個の部分として確認します。**

テスターは、Three.js の自転車に乗ったペリカンの出力が Neon によるものであると考えています。

作成者は録音を提供しますが、タイミングや推論の設定は提供しません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-9-1-80dcbc4fb2e8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-9-1-e0a6df02d79f.jpg" alt="Three.js でペリカンをアニメーション化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-10"></a>
### Case 10: [xhigh で SVG ポートレートを描画する](https://x.com/lyraxana/status/2123161268647539052) (by [@lyraxana](https://x.com/lyraxana))

**ポートレート テストで、らしさと SVG の編集可能性を個別に評価します。**

テスターは、Neon xhigh によるアナ デ アルマスの肖像画を共有しています。

ソースには、正確なプロンプトなしで件名と作業量の設定が示されています。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-10-1-014b0af2bac3.jpg" alt="xhigh で SVG ポートレートを描画する · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-11"></a>
### Case 11: [中程度の労力でサイクリング ペリカンをアニメーション化する](https://x.com/xiangning0/status/2123161354496557071) (by [@xiangning0](https://x.com/xiangning0))

**固定アニメーション タスクを使用して、さまざまな推論設定での結果を比較します。**

著者は Neon を中程度の労力で使用してペリカンのサイクリング デモを作成し、ビデオを投稿しました。

このクリップは、この作成者が一般的なテスト タスクを個別に実行した様子を記録しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-11-1-0b2be9516bad.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-11-1-200a792de0b6.jpg" alt="中程度の労力でサイクリング ペリカンをアニメーション化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-12"></a>
### Case 12: [2 つのボクセル ガーデン シーンを比較する](https://x.com/Angaisb_/status/2123161449681805531) (by [@Angaisb_](https://x.com/Angaisb_))

**総実行コストおよび各ソースが開示している設定と照らし合わせて、同様に見える出力を確認します。**

著者は、Neon xhigh のボクセル ガーデンを GPT-6.2 Sol xhigh の結果とともに投稿しました。

ソースは最初のイメージを Neon として識別し、Sol の場合は 1.01 米ドルであるのに対し、0.19 米ドルであると報告しています。この投稿では、プロンプトとツールが一致したかどうかは明らかにされていません。

<table>
<tr>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-12-1-115849b38af5.jpg" alt="2 つのボクセル ガーデン シーンを比較する · 1" width="560"></td>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-12-2-59e2b840c413.jpg" alt="2 つのボクセル ガーデン シーンを比較する · 2" width="560"></td>
</tr>
</table>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-13"></a>
### Case 13: [Three.js および GLSL シーンを生成する](https://x.com/cfenghub/status/2123162154132242885) (by [@cfenghub](https://x.com/cfenghub))

**グラフィックス テストでは、シェーダーの動作、シーンのジオメトリ、生成時間を個別に分離します。**

作成者は Neon からの Three.js と GLSL の出力を共有し、2 分 40 秒の実行を報告しています。

メインの投稿は、指示を引用することなく、指示に対する返信を指します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-13-1-e62c3cb9bbab.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-13-1-f2c7b50bad23.jpg" alt="Three.js および GLSL シーンを生成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-14"></a>
### Case 14: [完全にコードで絵画を作成する](https://x.com/kickingkeys/status/2123162238643044705) (by [@kickingkeys](https://x.com/kickingkeys))

**レンダリングされたサンプルを開いて、コードが一貫したビジュアル シリーズを生成する方法を確認します。**

作成者は、早期アクセスの Neon を使用して絵画をレンダリングするコードを作成したと報告しています。

ソースは、同じシリーズからの一連の結果を提供します。それぞれの正確なプロンプトは提供されません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-1-9f61a388e0c1.jpg" alt="完全にコードで絵画を作成する · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-2-3362674fdd00.jpg" alt="完全にコードで絵画を作成する · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-3-51899966784e.jpg" alt="完全にコードで絵画を作成する · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-4-74693c0f8c18.jpg" alt="完全にコードで絵画を作成する · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-5-977a643ac612.jpg" alt="完全にコードで絵画を作成する · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-6-74e97910a739.jpg" alt="完全にコードで絵画を作成する · 6" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-7-516b3420d145.jpg" alt="完全にコードで絵画を作成する · 7" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-8-7766df7b1a79.jpg" alt="完全にコードで絵画を作成する · 8" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-9-1a353988571a.jpg" alt="完全にコードで絵画を作成する · 9" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-10-57e623c52098.jpg" alt="完全にコードで絵画を作成する · 10" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-11-e9fe2e7b6c2c.jpg" alt="完全にコードで絵画を作成する · 11" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-14-12-2213841fb938.jpg" alt="完全にコードで絵画を作成する · 12" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-15"></a>
### Case 15: [ペリカンのサイクリングアニメーションを比較する](https://x.com/Super_Nius/status/2123162610254442796) (by [@Super_Nius](https://x.com/Super_Nius))

**報告されたランタイムを、同じビデオ内の動きやシーンの詳細と比較します。**

テスターは、Neon、Hydrogen、GPT-6.2 Astra、GPT-6.2 Sol のペリカン アニメーションを比較しました。

著者は、Neon を 3 分間実行したところ、その外観が気に入ったと報告しています。記録された Sol のみのフォローアップは同じテストに属します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-15-1-e9c127cb6e40.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-15-1-444e97e2290b.jpg" alt="ペリカンのサイクリングアニメーションを比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-16"></a>
### Case 16: [Three.js サイクリング アニメーションを 3 つのモデル間で比較](https://x.com/AI_Screening/status/2123164032882659819) (by [@AI_Screening](https://x.com/AI_Screening))

**ラベル付きクリップを使用して、モーション、ライティング、シーン構成を比較します。**

テスターは、Neon、Opus 5.5、および Carbon の Three.js サイクリング比較を公開しました。

筆者は Opus よりも Neon を好み、Carbon に近いと判断しました。これは著者の視覚的な評価です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-16-1-2fcea711afca.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-16-1-491c82d3f1f5.jpg" alt="Three.js サイクリング アニメーションを 3 つのモデル間で比較 · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-17"></a>
### Case 17: [海上の背の高い船をレンダリングします。](https://x.com/Mr_Salio/status/2123164576275370440) (by [@Mr_Salio](https://x.com/Mr_Salio))

**波のアニメーションと船のレンダリングがクリップ全体で一貫性を保っているかどうかを検査します。**

テスターは、Neon xhigh による海洋セーリング シーンを共有しました。

ビデオには帆船のアニメーションが表示されます。ソースは特定のワークフローやタイミングを提供していません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-17-1-39aa1af81d28.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-17-1-c2e29bd290ea.jpg" alt="海上の背の高い船をレンダリングします。 · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-18"></a>
### Case 18: [ボクセル パゴダを生成する](https://x.com/LuminaBench/status/2123164858996908367) (by [@LuminaBench](https://x.com/LuminaBench))

**ボクセル シーンを使用して、レイヤリング、シルエット、構成を評価します。**

テスターは、Neon xhigh で生成されたボクセル パゴダを投稿します。

この投稿には、レンダリング結果と作成者のデザイン上の反応が含まれています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-18-1-66d691af4081.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-18-1-8da133675a5d.jpg" alt="ボクセル パゴダを生成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-19"></a>
### Case 19: [自転車に乗ってイライラするペリカンを描く](https://x.com/HarshithLucky3/status/2123165824576114932) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**キャラクターの表情や自転車の動きなどが鮮明に読み取れるかどうかを確認します。**

作成者は AI Studio の Neon high を使用して、自転車に乗ってイライラするペリカンの SVG を描画しました。

この投稿には結果が表示され、労力設定が特定されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-19-1-44580d20f3b7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-19-1-b8df2a6ac156.jpg" alt="自転車に乗ってイライラするペリカンを描く · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-20"></a>
### Case 20: [ゲームパッドの描画を GPT-6.2 Sol と比較](https://x.com/notjazii/status/2123166093422272839) (by [@notjazii](https://x.com/notjazii))

**2 つのゲームパッド出力のレンダリング品質と時間とコストを個別に比較します。**

テスターは、各モデルの利用可能な最高の推論で同じプロンプトを使用し、出力が類似していると判断しました。

著者は、Neon では 20 分、約 1.60 米ドルであるのに対し、Sol では 9 分、約 0.53 米ドルであると報告しました。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-20-1-617938f21f28.jpg" alt="ゲームパッドの描画を GPT-6.2 Sol と比較 · 1" width="560">

Type: Evaluation | Date: 2026-11-18

---

<a id="case-21"></a>
### Case 21: [3D 水上飛行機を生成する](https://x.com/LuminaBench/status/2123166304664191391) (by [@LuminaBench](https://x.com/LuminaBench))

**プロトタイプ全体を判断する前に、水上飛行機と水の相互作用を確認してください。**

テスターは Neon xhigh を使用して 3D 水上飛行機を構築し、ビデオを共有しました。

作成者は、実測値を示さずに、ビルドが速く、インターフェイスがクリーンであると述べています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-21-1-738f7ccd5e11.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-21-1-b2943474925e.jpg" alt="3D 水上飛行機を生成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-22"></a>
### Case 22: [2D の馬を描く](https://x.com/jony_palino/status/2123168463640269001) (by [@jony_palino](https://x.com/jony_palino))

**馬のクリップを視覚的な例として扱い、モデル間の設定を念頭に置いてください。**

作者はNeonを使って二次元の馬を制作し、その出力物を投稿しました。

作成者は、以前の Gemini の結果よりもそれを好みました。投稿には一致する設定が提供されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-22-1-0806852b6c63.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-22-1-e4f265e40f74.jpg" alt="2D の馬を描く · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-23"></a>
### Case 23: [雨のコンビニシーンをテストしてみる](https://x.com/Super_Nius/status/2123169627815698522) (by [@Super_Nius](https://x.com/Super_Nius))

**一致したシーンを使用して、より短い生成時間でプレゼンテーションがどのように変化するかを評価します。**

テスターは Neon と GPT-6.2 Sol に対して同じプロンプトを使用し、比較を投稿しました。

著者は、この実行では Neon のより速く、より安価な完了を報告しながら、Sol のビジュアル出力を好みました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-23-1-9e27412d4ad5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-23-1-d8e64f437d92.jpg" alt="雨のコンビニシーンをテストしてみる · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-24"></a>
### Case 24: [1 つの画像から四足歩行のロボットをアニメーション化する](https://x.com/thebuggeddev/status/2123170821250400282) (by [@thebuggeddev](https://x.com/thebuggeddev))

**シーンが基準にどれだけ忠実に従っているかとは別に、歩行と動きをチェックします。**

開発者は Neon に 1 つの参考画像を与え、3D モデルを要求しました。

開発者は、4 脚の逆運動学と歩行、速歩、ギャロップのアニメーションを使用した Three.js WebGPU のデモを報告します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-24-1-acb1deb37714.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-24-1-22e170b487dd.jpg" alt="1 つの画像から四足歩行のロボットをアニメーション化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-25"></a>
### Case 25: [バニラ JavaScript で Keats をアニメーション化する](https://x.com/vamsibatchuk/status/2123170948568535488) (by [@GeokenAI](https://x.com/GeokenAI))

**コードを使用して文学ソースを解釈する場合、アニメーションと筆致を比較してください。**

Google チームのメンバーは、Keats の To Autumn のバニラ JavaScript アニメーションについては、GeokenAI と Neon の功績を認めています。

この投稿では、ライブラリを使用しない 12 fps の絵画風の 3D アニメーションについて説明しています。共有アカウントは、クレジットされたクリエイターとは異なります。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-25-1-251f0dd0d495.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-25-1-3927f6ba8991.jpg" alt="バニラ JavaScript で Keats をアニメーション化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-26"></a>
### Case 26: [トリケラトプスのデモを作成する](https://x.com/LeslieNooteboom/status/2123171009167765651) (by [@LeslieNooteboom](https://x.com/LeslieNooteboom))

**再構成シーケンスと最終的なビジュアルを検査します。**

作成者は、トリケラトプスのデモンストレーションは Neon によるものだと考えています。

ビデオではアーティファクトが示されています。この投稿では、入力形式や生成手順は指定されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-26-1-8c4ac6bb4433.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-26-1-e0d7589c04bb.jpg" alt="トリケラトプスのデモを作成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-27"></a>
### Case 27: [3D 歯車列レンダリングを比較する](https://x.com/SPAC89/status/2123171830739632189) (by [@SPAC89](https://x.com/SPAC89))

**ラベル付きの設定と出力ジオメトリを使用して、4 つのギア トレイン レンダリングをすべて比較します。**

テスターは、ラベル付き推論レベル全体で Neon、Carbon、Astra、Sol の歯車機構のレンダリングを表示します。

筆者はNeonを愛用していました。このクリップは 1 つの視覚的な比較を記録したものであり、一般的なコストの主張を確立するものではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-27-1-94516eb237d5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-27-1-c7804af5b07a.jpg" alt="3D 歯車列レンダリングを比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-28"></a>
### Case 28: [1 つの HTML ファイルで 10 個のインタラクティブなエフェクトを作成する](https://x.com/agenticjay/status/2123172043533508664) (by [@agenticjay](https://x.com/agenticjay))

**小さな HTML ペイロード内でエフェクトの応答性と読み取り可能性が維持されているかどうかを確認します。**

Google チームのメンバーは、Neon を使用して 1 つの 27 KB HTML ファイルに 10 個のインタラクティブ 3D 効果を作成したと報告しています。

デモにはシェーダー、水、照明が含まれています。バリエーションは 1 つの公開プロジェクトとしてグループ化されます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-28-1-7af28a595410.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-28-1-91d62f30b2e1.jpg" alt="1 つの HTML ファイルで 10 個のインタラクティブなエフェクトを作成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-29"></a>
### Case 29: [Antigravity Swarm を使用して Blender ラボベンチを構築する](https://x.com/Google/status/2123172290250621166) (by [@Google](https://x.com/Google))

**Swarm がどの作業を調整し、Blender がどの操作を実行するかをトレースします。**

Google は、Antigravity Swarm と Blender を使用して Gemini 4 ファミリーをテーマにした実験台のシーンを作成する Neon をデモンストレーションしました。

このクリップは、統合ワークフローのプロバイダーのデモです。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-29-1-24f7c4b89ee2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-29-1-5515f85f88ea.jpg" alt="Antigravity Swarm を使用して Blender ラボベンチを構築する · 1" width="560"></a>

Type: Integration | Date: 2026-11-18

---

<a id="case-30"></a>
### Case 30: [建築イラストと Opus 5.5 を比較する](https://x.com/notjazii/status/2123172429791129848) (by [@notjazii](https://x.com/notjazii))

**同じビジュアル タスクを設定し、出力品質、実行時間、コストを個別に比較します。**

テスターは、同じプロンプトを使用して、可能な限り最高の推論を使用してモデルを比較しました。

著者は、Neon では約 20 分で 3.50 米ドル、Opus では 18 分で 7.20 米ドルであると報告し、Opus の出力を好みました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-30-1-b5e87dfb79f7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-30-1-b13b60aca1f2.jpg" alt="建築イラストと Opus 5.5 を比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-31"></a>
### Case 31: [ボイジャー1号の飛行を可視化する](https://x.com/SamuelAlbanie/status/2123174398064570622) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**シーケンスを判断する際には、打ち上げ、フライバイ、クローズアップの間のトランジションを確認してください。**

著者は、打ち上げから木星との遭遇までのボイジャー 1 号の 3D シーケンスと探査機のクローズアップを示しています。

著者はこれをシリーズの中での洗練されていないプロンプトの 1 つであると説明しています。軌道の検証は報告されません。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-31-1-2819a8649adb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-31-1-49c120f1aa13.jpg" alt="ボイジャー1号の飛行を可視化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-32"></a>
### Case 32: [3Dプラネタリウムを作る](https://x.com/SamuelAlbanie/status/2123174400572719261) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**惑星と星座のビューが簡単な教育用デモとして連携して機能するかどうかを確認します。**

著者は、惑星間を移動する 3D プラネタリウムと星座ビューを示しています。

記録には地球や土星などの例が示されています。ワンプロンプトシリーズでは天文学的な精度は確立されません。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-32-1-3744b688f28d.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-32-1-f238cb6328df.jpg" alt="3Dプラネタリウムを作る · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-33"></a>
### Case 33: [バベッジの階差機関第2号を可視化する](https://x.com/SamuelAlbanie/status/2123174403038982379) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**ビジュアライゼーションを確認するときは、ギアの動き、数値表示、およびマシン全体のビューを確認してください。**

著者は、ギア アセンブリと数値表示を備えたバベッジのディファレンス エンジン No. 2 の 3D 視覚化を示しています。

録画は、移動機構のクローズアップと完全な機械のビューの間を移動します。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-33-1-8f8b964cd1a7.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-33-1-e80ac8cce5ad.jpg" alt="バベッジの階差機関第2号を可視化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-34"></a>
### Case 34: [アンティキティラ島の機械を可視化する](https://x.com/SamuelAlbanie/status/2123174406419828813) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**同じデモで、復元された断片の表示、ギアの再構成、ダイヤルの読み出しを比較します。**

著者は、回収された物体、復元された歯車、ダイヤルを切り替える 3D アンティキティラ メカニズムのデモを示しています。

録画には、組み立ての表示と移動機構の詳細が表示されます。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-34-1-de291a3cf77f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-34-1-8f404bea04c4.jpg" alt="アンティキティラ島の機械を可視化する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-35"></a>
### Case 35: [気流を可視化する風洞の試作を作る](https://x.com/SamuelAlbanie/status/2123174409284260270) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**視覚化を教育例として使用する前に、テスト形状間で流線がどのように変化するかを比較してください。**

著者は、さまざまな形状の周りに目に見える空気の流れの流線を備えた 3D 風洞デモを示しています。

ビデオには航空機やその他のテスト形状が含まれています。シミュレーションに対して独立した精度チェックは行われません。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-35-1-9424d7eab5ec.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-35-1-acc3f3a6f94a.jpg" alt="気流を可視化する風洞の試作を作る · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-36"></a>
### Case 36: [キングス・カレッジ礼拝堂の断面を再現する](https://x.com/SamuelAlbanie/status/2123174412488716605) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**外観、身廊、断面図を比較して、それぞれのビューが建物をどのように説明しているかを確認してください。**

著者は、外部と内部が切り替わるキングス カレッジ礼拝堂の 3D 断面図を示しています。

このシーンでは、さまざまなビューを使用して、身廊、窓、建物の断面を表示します。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-36-1-8c718b6a7b3c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-36-1-72acb7ce83d2.jpg" alt="キングス・カレッジ礼拝堂の断面を再現する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-37"></a>
### Case 37: [川に架かる高架橋と周辺を描画する](https://x.com/SamuelAlbanie/status/2123174416154759418) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**近く、遠く、ワイヤーフレームのビューを使用して、橋とその周囲のシーンの両方を評価します。**

著者は、マルチアーチ高架橋、列車、およびいくつかのレンダリング ビューを備えた 3D の川の渓谷を示しています。

録画では、近くと遠くのカメラ アングルが切り替わり、ワイヤーフレームのようなビューが含まれます。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-37-1-d12ab14ffcb0.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-37-1-56962c64e01c.jpg" alt="川に架かる高架橋と周辺を描画する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-38"></a>
### Case 38: [ケンブリッジを思わせる3Dの街並みを作る](https://x.com/SamuelAlbanie/status/2123174419379962139) (by [@SamuelAlbanie](https://x.com/SamuelAlbanie))

**カメラがシーン内を移動するときに、ランドマークと川がどのように認識され続けるかを確認します。**

著者は、ケンブリッジにインスピレーションを得た都市のビジュアライゼーションを、モデル化された街区の上空からの眺めとより近い視点で示しています。

このクリップには、川、建物、シーンのオーバーレイが表示されます。著者はこの設定をケンブリッジに似ていると述べています。

[補足資料](https://x.com/SamuelAlbanie/status/2123174391617867925)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-38-1-731938345922.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-38-1-fdabb0976ddb.jpg" alt="ケンブリッジを思わせる3Dの街並みを作る · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-39"></a>
### Case 39: [ネオンをテーマにした地球をレンダリングする](https://x.com/HarshithLucky3/status/2123175900007309696) (by [@HarshithLucky3](https://x.com/HarshithLucky3))

**地球が回転してもビジュアルテーマが一貫しているかどうかを確認します。**

作者は Antigravity で Neon の High 設定を使い、ネオンをテーマにした地球をレンダリングしました。

ソースは結果と労力の設定を提供します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-39-1-b5f3ce29cb24.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-39-1-113aeb084222.jpg" alt="ネオンをテーマにした地球をレンダリングする · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-40"></a>
### Case 40: [ヨットのシーンを反復する](https://x.com/LyalinDotCom/status/2123176455123165366) (by [@LyalinDotCom](https://x.com/LyalinDotCom))

**モデルに 3D シーンの調整を依頼するときは、前後のアーティファクトを確認してください。**

作成者は、Neon がヨット シーンを改善したと報告し、その出力を示しています。

Firebase のデプロイは、投稿時点で明示された意図でした。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-40-1-367b9069fe9e.jpg" alt="ヨットのシーンを反復する · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-41"></a>
### Case 41: [カスタム VFX ツールで衣装素材を作成する](https://x.com/fofrAI/status/2123176812360745019) (by [@fofrAI](https://x.com/fofrAI))

**素材を選ぶ際には、同じ衣装形状の処理を比較してください。**

作者は Neon を使って衣装素材を作成し、その結果の画像 6 枚を投稿しました。

制作者は、VFX ツールを独自のものとして説明しています。この情報源は独立したパフォーマンス比較を確立していません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-1-ec60d5cf5112.jpg" alt="カスタム VFX ツールで衣装素材を作成する · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-2-88c3a0c15c9e.jpg" alt="カスタム VFX ツールで衣装素材を作成する · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-3-a6a770888735.jpg" alt="カスタム VFX ツールで衣装素材を作成する · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-4-66dd457d66be.jpg" alt="カスタム VFX ツールで衣装素材を作成する · 4" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-5-adda34356599.jpg" alt="カスタム VFX ツールで衣装素材を作成する · 5" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-41-6-4dbc04fb999c.jpg" alt="カスタム VFX ツールで衣装素材を作成する · 6" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-42"></a>
### Case 42: [ボクセルNinjagoシーンの比較](https://x.com/thehypedotnews/status/2123182627674796462) (by [@thehypedotnews](https://x.com/thehypedotnews))

**同じ被写体のボクセルを比較して、視覚的なフレーミングとコストを個別に判断します。**

ソースでは、ボクセル再現で Neon と Fable 5.2 を比較しています。

著者は、Neon が 12.93 ドル、Fable が 11.19 ドルであると報告しており、後者のフレームを好みました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-42-1-e2257b7ed90f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-42-1-1c3b543e0111.jpg" alt="ボクセルNinjagoシーンの比較 · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-43"></a>
### Case 43: [ペリカン製品のモーショングラフィックを作成する](https://x.com/chetaslua/status/2123184113561817370) (by [@chetaslua](https://x.com/chetaslua))

**短い製品アニメーションでタイミングとタイポグラフィーを一緒に見てください。**

制作者は、ペリカンをテーマにした製品のモーション グラフィックを Neon に提供したと認めています。

リンクされたクリップは出力を示しています。この投稿では、実装や正確なプロンプトについては説明されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-43-1-41540f06843a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-43-1-d81b2060fc29.jpg" alt="ペリカン製品のモーショングラフィックを作成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-44"></a>
### Case 44: [ニューヨーク市のシーンのプロトタイプを比較する](https://x.com/aipulseda1ly/status/2123188460639117489) (by [@aipulseda1ly](https://x.com/aipulseda1ly))

**都市シーンのビルドでランドマークの忠実性と実行時のパフォーマンスを個別に評価します。**

テスターの報告によると、Neon にはブルックリン橋、自由の女神、タクシーが通る通りが含まれていました。

テスターは、Opus 出力の一部の詳細を好み、Neon シーンの実行が PC に遅れると報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-44-1-85f5c28fc00c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-44-1-7a276a2045df.jpg" alt="ニューヨーク市のシーンのプロトタイプを比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-45"></a>
### Case 45: [バナナのビジュアルテストを実行する](https://x.com/AdamHoltererer/status/2123189288107999706) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**単純な視覚的タスクが詳細と比率にわたってどのように維持されるかを検査します。**

テスターは、Banana Test というタイトルのテストの Neon 出力を投稿します。

出力はソースに接続されます。ソースには正確なプロンプトが提供されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-45-1-9efc4470be00.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-45-1-c82bae60d92d.jpg" alt="バナナのビジュアルテストを実行する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-46"></a>
### Case 46: [幽霊が出る大聖堂を 1 つのプロンプトで比較する](https://x.com/jan_volad/status/2123205954649100424) (by [@jan_volad](https://x.com/jan_volad))

**公開されたプロンプトを使用して、説明されている条件下での 2 つの大聖堂のレンダリングを比較します。**

テスターは Neon と GPT-6.2 Sol に同じ幽霊の大聖堂のタスクを与えました。

作成者は、Neon が 2.67 米ドル、Sol が 1.69 米ドルであると報告していますが、評価では視覚的に明確な勝者はいません。

**Prompt:**

```
Build a huge haunted vampire cathedral
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-46-1-c1293f480928.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-46-1-8adbefb0cdfe.jpg" alt="幽霊が出る大聖堂を 1 つのプロンプトで比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-47"></a>
### Case 47: [Antigravity で電話アセンブリのプロトタイプを作成する](https://x.com/ai_for_success/status/2123207149870547423) (by [@ai_for_success](https://x.com/ai_for_success))

**設計プロトタイプをレビューするときは、コンポーネントの忠実性と最終アセンブリを個別にチェックします。**

開発者は Antigravity で Neon を使用し、設計コンポーネントのボードとレンダリングされた電話アセンブリを示しました。

開発者は、タイミングや管理された Carbon 比較を行わずに、コーディングと速度の初期の印象を報告します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-47-1-188cdb56dd8e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-47-1-e54b9bc965db.jpg" alt="Antigravity で電話アセンブリのプロトタイプを作成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-48"></a>
### Case 48: [インタラクティブな歴史的帆船を生成する](https://x.com/abhinavflac/status/2123212198663323848) (by [@abhinavflac](https://x.com/abhinavflac))

**インタラクティブな出力で船と水の間の境界を検査します。**

著者はゼロショット 3D 帆船のデモンストレーションを投稿しました。

著者は、船と水が別個のレイヤーでレンダリングされたことを報告し、その出力が Sol の結果よりも現実的であると説明しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-48-1-8398538c7634.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-48-1-19d730412b53.jpg" alt="インタラクティブな歴史的帆船を生成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-49"></a>
### Case 49: [JavaScript でモデル導入を設計する](https://x.com/chetaslua/status/2123219124260315301) (by [@chetaslua](https://x.com/chetaslua))

**JavaScript モーション グラフィックのタイポグラフィとペースを確認します。**

著者は Neon を使用してモデルを紹介するモーション グラフィックを作成しました。

著者によれば、外部アセットを使用せずに JavaScript を使用しているとのことです。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-49-1-640c76599969.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-49-1-213f5084a7a0.jpg" alt="JavaScript でモデル導入を設計する · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-50"></a>
### Case 50: [スキー小屋のシーンを 1 つのパスで生成する](https://x.com/DesignArena/status/2123220446074253768) (by [@DesignArena](https://x.com/DesignArena))

**このワンパス シーンの比較を評価するときは、小屋、雪、木を個別に確認してください。**

DesignArena は、Neon と Argon に同じアルプス小屋の設定を生成するよう依頼し、並べて出力したものを公開しました。

DesignArena は両方のレンダリングの要素を優先します。 Neon が断りもなく降雪を追加したと報告しています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-50-1-a966b54bde0e.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-50-1-d867d8d5e6d7.jpg" alt="スキー小屋のシーンを 1 つのパスで生成する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-51"></a>
### Case 51: [ボクセルのファンタジー城をレンダリングする](https://x.com/Lentils80/status/2123226306351661099) (by [@Lentils80](https://x.com/Lentils80))

**ワンプロンプト ビルドを評価する場合は、最終シーンと報告された実行時間を確認してください。**

作成者は、Neon xhigh で作成されたボクセル城を共有しています。

作成者は、1 つのプロンプトと 27 分の完了時間を報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-51-1-27fe32067ec9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-51-1-e38a5f2c5e9e.jpg" alt="ボクセルのファンタジー城をレンダリングする · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-52"></a>
### Case 52: [タコのサイクリングアニメーションをAstraと比較してください](https://x.com/ZryMiller/status/2123228351984980040) (by [@ZryMiller](https://x.com/ZryMiller))

**2 つの推論設定を明示的に保ちながら、アニメーションとコストを比較します。**

検証者の記録では、Astra (xhigh) は 21 分 53 秒で 2.52 米ドル、Neon (high) は 41 分で 4.02 米ドルでした。

著者はアニメーションの品質を近いと呼んでいます。これは、さまざまな推論設定での 1 つの実行です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-52-1-0039f05541ac.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-52-1-546dd90156c6.jpg" alt="タコのサイクリングアニメーションをAstraと比較してください · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-53"></a>
### Case 53: [Three.js 蝶のアニメーション](https://x.com/thtbee_/status/2123259795172212871) (by [@thtbee_](https://x.com/thtbee_))

**クリップとその報告されたリソース使用量を使用して、同様の Three.js 実験のサイズを決定します。**

クリエイターは Antigravity の Neon xhigh を使用して Three.js の蝶のアニメーションを作成しました。

作成者は 57 分、5 時間のノルマの約 23%、週のノルマの 7% を報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-53-1-efb25e8f446f.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-53-1-7a50c0010ea3.jpg" alt="Three.js 蝶のアニメーション · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-54"></a>
### Case 54: [参照画像からコンポーネントとモーションを構築する](https://x.com/op7418/status/2123269503736070603) (by [@op7418](https://x.com/op7418))

**視覚的な参照を提供し、レイアウトの忠実度と動きを別の基準として評価します。**

作成者は視覚的な参照を使用して、いくつかのコンポーネントとそれに伴うモーションを生成しました。

デモでは結果が示されています。 Opusと比べてどのように感じるかについての主張は作成者の判断です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-54-1-aab23e8d82f9.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-54-1-c4200a430fb5.jpg" alt="参照画像からコンポーネントとモーションを構築する · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-55"></a>
### Case 55: [Three.js のピクセル ウィザードの世界](https://x.com/thtbee_/status/2123279727935033355) (by [@thtbee_](https://x.com/thtbee_))

**3 つのパスを使用して、反復によって視覚的な磨きがどのように変化するかを判断します。**

作成者は Neon の参考画像を提供し、3 回のパスにわたって Three.js シーンを改良しました。

作成者は、Antigravity で 5 時間の割り当ての 39% と 1 週間の割り当ての 11% を使用したと報告しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-55-1-ea88133798aa.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-55-1-bdca3bf63f42.jpg" alt="Three.js のピクセル ウィザードの世界 · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-56"></a>
### Case 56: [城のレンダリングベンチマーク](https://x.com/nemumusitocha/status/2123287660525719823) (by [@nemumusitocha](https://x.com/nemumusitocha))

**城を 1 人のクリエイターの視覚的なベンチマークとして扱い、アカウント固有の割り当てコンテキストを保持します。**

作者は Neon を城のベンチマークに使用し、動画と静止画を投稿しました。

作成者は、プランの週間割り当ての約 4% を使用したと報告しました。この投稿では、その使用法が他のアカウントにも一般化するかどうかは明らかにされていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-56-1-74e98240a81a.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-56-1-17acc3f87741.jpg" alt="城のレンダリングベンチマーク · 1" width="560"></a>
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-56-2-b4f97941d7b2.jpg" alt="城のレンダリングベンチマーク · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-56-3-05bccf69bb0c.jpg" alt="城のレンダリングベンチマーク · 3" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-56-4-a8081504106d.jpg" alt="城のレンダリングベンチマーク · 4" width="560">

Type: Evaluation | Date: 2026-11-19

---

<a id="case-57"></a>
### Case 57: [アラン・チューリングの1936年当時の書斎を再現する](https://x.com/GoogleAI/status/2123168242797809944) (by [@GoogleAI](https://x.com/GoogleAI))

**再構築の別個の部分として、アーカイブの忠実性とインタラクティブな機能をチェックします。**

Google は、Neon と Antigravity Swarm を使用して、アーカイブ写真からインタラクティブな再構成を構築しました。

このシーンには、王の礼拝堂、チューリングの書斎、机の上の万能チューリング マシンの動作シミュレーションが含まれています。

[補足資料](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

[補足資料](https://www.youtube.com/watch?v=KgLLa4WhMSo)

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-57-1-22665c6264ea.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-57-1-b7fab25c354f.jpg" alt="アラン・チューリングの1936年当時の書斎を再現する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

## 🎮 ゲームとシミュレーション
<a id="games"></a>

<a id="case-58"></a>
### Case 58: [横スクロール障害物ゲームを構築する](https://x.com/notjazii/status/2123162053292458218) (by [@notjazii](https://x.com/notjazii))

**小さなゲームのプロトタイプをレビューするときに、障害物ループと衝突の動作をテストします。**

テスターは Neon に Flappy Bird スタイルのプロトタイプを依頼し、その録音を投稿しました。

著者が約 5 分間のレポートを作成し、コストや使用方法についての独自の感想を述べます。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-58-1-9c665bbec561.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-58-1-316557add829.jpg" alt="横スクロール障害物ゲームを構築する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-59"></a>
### Case 59: [剣と盾の戦闘シーンを比較](https://x.com/IndependentEco/status/2123169526619758996) (by [@IndependentEco](https://x.com/IndependentEco))

**2 つのラベル付きクリップを使用して、視覚的およびインタラクションの違いをご自身で評価してください。**

テスターは、戦闘ゲーム シーンの Fable 5.2 および Neon 出力のラベルが付いたビデオを投稿しました。

ビデオには 2 つの結果が記録されており、一般的なモデルのランキングを確立するものではありません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-59-1-ba79ec8e02b6.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-59-1-8644c701cdea.jpg" alt="剣と盾の戦闘シーンを比較 · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-60"></a>
### Case 60: [シンセウェーブ風のミニゴルフゲームを作る](https://x.com/antigravity/status/2123176067380711725) (by [@antigravity](https://x.com/antigravity))

**エージェントが作業をどう分担し、ブラウザーで全 8 コースをどう検証するかを確認する。**

Google Antigravity は、Gemini 4 Neon が Swarm を使い、1 つのプロンプトから 3D ミニゴルフゲームを作る様子を公開した。

映像には、8 つの作業エージェント、ブラウザーでのプレイ、組み込みの検証機能による全 8 コースの確認が映っている。

**Prompt:**

```
Build NEONPUTT '84: a 2-player synthwave 3D mini golf game with custom GLSL shaders, 240Hz fixed-timestep physics, procedural Web Audio SFX, and 8 animated courses.
```

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-60-1-bb8fa045c256.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-60-1-aabeaf2b1557.jpg" alt="シンセウェーブ風のミニゴルフゲームを作る · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-61"></a>
### Case 61: [アニメの騎士の決闘を比較する](https://x.com/IndependentEco/status/2123177347046355324) (by [@IndependentEco](https://x.com/IndependentEco))

**2 つのデュエル クリップのモーションの読みやすさとキャラクターのステージングを比較してください。**

テスターは、装甲キャラクター間の決闘用に、ラベル付きの Opus 5.5 と Neon の出力を別々に投稿しました。

この投稿では、レンダリングされた結果を判断するよう読者に求めており、制御されたプロトコルは開示されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-61-1-e225fa617e25.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-61-1-9759ab506b69.jpg" alt="アニメの騎士の決闘を比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-62"></a>
### Case 62: [1 つの HTML ファイルで表現主義アート ゲームを作成する](https://x.com/GeokenAI/status/2123178088439959750) (by [@GeokenAI](https://x.com/GeokenAI))

**1 つの HTML ファイルとして配信されるゲームのビジュアル スタイルとコントロールを検査します。**

開発者は Neon を使用して、1 つの HTML ファイルに含まれるエンドレスの JavaScript アート ゲームを作成しました。

開発者は結果を公開し、その表現主義的な視覚処理について説明しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-62-1-2f66690ce4f1.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-62-1-c9b9995f7891.jpg" alt="1 つの HTML ファイルで表現主義アート ゲームを作成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-63"></a>
### Case 63: [アイスボス ゲームのプロトタイプを比較する](https://x.com/IndependentEco/status/2123187721040503097) (by [@IndependentEco](https://x.com/IndependentEco))

**ラベル付き遭遇映像を使用して、共有プロンプトを想定せずにシーンの読みやすさを判断します。**

テスターは、一人称アイスボスとの遭遇用に、ラベル付きの Neon および Opus 5.5 出力を投稿しました。

ビデオでは視覚的に比較できます。投稿では、プロンプト、設定、タイミング、勝者が未設定のままになります。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-63-1-698acd0d6e0b.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-63-1-ebb40849a72b.jpg" alt="アイスボス ゲームのプロトタイプを比較する · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-64"></a>
### Case 64: [スイカバスケットボールのデモ](https://x.com/AdamHoltererer/status/2123189375831859349) (by [@AdamHoltererer](https://x.com/AdamHoltererer))

**このプロトタイプでアリーナ、動き、ボールの相互作用を確認してください。**

テスターは Neon スイカ バスケットボールのビデオを共有しています。

作成者はテストされたモデルに名前を付け、結果をリンクしますが、タイミングやビルド設定は提供しません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-64-1-12fdea478ad2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-64-1-832287da058f.jpg" alt="スイカバスケットボールのデモ · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-65"></a>
### Case 65: [ガウス スプラッティング ベーカリー プラットフォーマーを構築する](https://x.com/GlitterPixely/status/2123235794747891968) (by [@GlitterPixely](https://x.com/GlitterPixely))

**記録されたプレイスルーを使用して、レンダリング作業とゲームプレイの調整を区別します。**

作成者は Neon を使用して、C++20 と WebGPU のガウス スプラッティング エンジンを 4 タワー プラットフォーマーに変えました。

作成者は 3 つのプロンプトと約 60 分のアクティブな群時間を報告し、モデルにデモを記録するよう依頼しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-65-1-02f40215c097.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-65-1-df9397699125.jpg" alt="ガウス スプラッティング ベーカリー プラットフォーマーを構築する · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-66"></a>
### Case 66: [Antigravity Swarm で 3D ゲームを構築する](https://x.com/ai_for_success/status/2123239282626478306) (by [@ai_for_success](https://x.com/ai_for_success))

**Swarm 支援ビルドで、結果として得られるモバイル パスとデスクトップ パスを個別に確認します。**

開発者は Neon と Antigravity Swarm を使用して小さな 3D ゲームを構築しました。

開発者はモバイルとデスクトップの両方のサポートについて説明し、ウォークスルー スレッドを共有します。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-66-1-ec1085204901.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-66-1-63e6c5c75657.jpg" alt="Antigravity Swarm で 3D ゲームを構築する · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-67"></a>
### Case 67: [宇宙レーシングプロトタイプ](https://x.com/badboyfoxy/status/2123251809183785076) (by [@badboyfoxy](https://x.com/badboyfoxy))

**プレイアブル結果を、報告された最初のビルドの時間とコストと比較します。**

クリエイターは、Neon を使用してスペース レーサーを高い推論で構築したと報告しました。

作成者は、1.50 米ドルの費用がかかる約 15 分の実行を報告し、その出力を投稿しました。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-67-1-538f36726201.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-67-1-22fc51387262.jpg" alt="宇宙レーシングプロトタイプ · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-68"></a>
### Case 68: [タワーディフェンスのプロトタイプ](https://x.com/DeryaTR_/status/2123276863481254210) (by [@DeryaTR_](https://x.com/DeryaTR_))

**著者の滑らかさのレポートから一般化する前に、タワーディフェンスループを自分でテストしてください。**

開発者は、Neon で構築されたタワーディフェンス プロトタイプのゲームプレイを投稿しました。

開発者は、5 時間の割り当ての約 20 分と 2% を報告しました。スムーズなプレイの主張は開発者の評価です。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-68-1-4fadc1a0a053.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-68-1-9adcd74642bd.jpg" alt="タワーディフェンスのプロトタイプ · 1" width="560"></a>

Type: Demo | Date: 2026-11-19

---

<a id="case-69"></a>
### Case 69: [一人称視点のスキー シミュレーターを構築する](https://www.youtube.com/watch?v=xhG-jNObuz4) (by [@Google](https://blog.google/))

**スキー シミュレーターを評価するときは、地形、動き、音声を個別に検討してください。**

Google は、Neon を使用してモンブランとシャモニーの地形で WebGL2 フリーライド シミュレーターを作成したと報告しています。

このデモンストレーションには、6 つのスキー ライン、120 Hz 物理ループ、トラック カービング、空間オーディオが含まれます。

[補足資料](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

<a href="https://www.youtube.com/watch?v=xhG-jNObuz4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-69-1-42268a3924ba.jpg" alt="一人称視点のスキー シミュレーターを構築する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

## 📚 知識労働
<a id="knowledge"></a>

<a id="case-70"></a>
### Case 70: [モデルの選択を調査表に要約する](https://x.com/Arcadia_Bao/status/2123171058002088343) (by [@Arcadia_Bao](https://x.com/Arcadia_Bao))

**モデル選択テーブルを使用して決定する前に、モデル選択テーブルの主張を情報源と照らし合わせて検証してください。**

著者は、Gemini 4 モデル選択テーブルは Neon によって実行された研究によるものであると考えています。

スクリーンショットは、結果として得られる推奨事項です。そのエントリは調査タスクの結果であり、独自に検証された製品ガイダンスではありません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-70-1-220032ad276d.jpg" alt="モデルの選択を調査表に要約する · 1" width="560">

Type: Demo | Date: 2026-11-18

---

<a id="case-71"></a>
### Case 71: [Neon とローンチ フィルムを共同作成する](https://x.com/gracepursuits/status/2123190512853176421) (by [@gracepursuits](https://x.com/gracepursuits))

**この映画をプロバイダーの例として使用し、制作ステップを特定する前に他のツールを特定します。**

Google チームのメンバーが Neon と映画を共同制作したことを報告し、その結果を共有します。

この映画はプロバイダー側​​のデモンストレーションです。この投稿では、どのツールが個々のフレームや音声をレンダリングしたかは特定されていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-71-1-b0eb81c105f2.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-71-1-aef8fd5224ef.jpg" alt="Neon とローンチ フィルムを共同作成する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-72"></a>
### Case 72: [VR ゲームの機器の仕組みを説明する](https://x.com/Msfs2000J/status/2123201737217773826) (by [@Msfs2000J](https://x.com/Msfs2000J))

**ガイドとして扱う前に、説明上のアーティファクトをゲームの仕組みと照らし合わせて確認してください。**

筆者はメタクエストゲームH3VR2の装備をNeonを使ってまとめ、図解付きの解説をつけました。

アーティファクトはゲームのシナリオを文書化します。情報源は正確なプロンプトを特定しておらず、ビデオ制作を Neon に割り当てていません。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-72-1-edea62f20bb5.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-72-1-b669c1f763a7.jpg" alt="VR ゲームの機器の仕組みを説明する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

<a id="case-73"></a>
### Case 73: [画像のトリミング中に自己評価を検査する](https://x.com/viticci/status/2123208444681372133) (by [@viticci](https://x.com/viticci))

**モデルの品質の説明に頼る前に、作物自体を判断してください。**

テスターは、画像編集テスト中に Neon が自身の作物を補完したと報告しました。

スクリーンショットは 1 回のやり取りを示しています。画像の切り抜き品質や、ほかのツールでの挙動は判断できません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-73-1-be1d8691e528.jpg" alt="画像のトリミング中に自己評価を検査する · 1" width="560">

Type: Limit | Date: 2026-11-19

---

<a id="case-74"></a>
### Case 74: [記事を編集可能なスライドに変換する](https://x.com/tetumemo/status/2123210419137601764) (by [@tetumemo](https://x.com/tetumemo))

**スライドが編集可能であること、およびスライドの画像が元の記事をサポートしていることを確認してください。**

作成者は Neon に記事を送信し、公開スライド作成スキルを使用しました。

作成者は、ワークフローによって画像が生成および挿入され、編集可能な Google スライドが配信されたと報告しています。この投稿では、画像ジェネレーターを特定せずに、全体的なワークフローについて説明します。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-74-1-b1cfed0393a4.jpg" alt="記事を編集可能なスライドに変換する · 1" width="560">

Type: Demo | Date: 2026-11-19

---

<a id="case-75"></a>
### Case 75: [ファンタジー小説のオープニングを生成する](https://x.com/Arcadia_Bao/status/2123222272697913481) (by [@Arcadia_Bao](https://x.com/Arcadia_Bao))

**長い草稿について結論を出す前に、冒頭のスタイルと声を確認してください。**

著者は、Neon をライティング テストに使用し、中国のファンタジー物語の冒頭を公開しました。

この投稿には、完成した冒頭部分の抜粋が示されています。その長さと品質は、モデルの長い形式のパフォーマンスを確立するものではありません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-75-1-142f892ae717.jpg" alt="ファンタジー小説のオープニングを生成する · 1" width="560">

Type: Demo | Date: 2026-11-19

---

<a id="case-76"></a>
### Case 76: [オリジナルのダリオジョークを解釈する](https://x.com/MichaelLee009/status/2123236918456733855) (by [@MichaelLee009](https://x.com/MichaelLee009))

**一致した例を使用して、特定のジョークの理解と広範な文章能力を区別します。**

著者は、Neon は自分たちが書いたジョークを理解したが、Opus 5.5 は理解できなかったと報告しています。

これはスクリーンショットを使った試みです。広範な文章や推論のパフォーマンスを確立するものではありません。

<table>
<tr>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-76-1-0e02d7ae6f39.jpg" alt="オリジナルのダリオジョークを解釈する · 1" width="560"></td>
<td><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-76-2-d1e4fd891049.jpg" alt="オリジナルのダリオジョークを解釈する · 2" width="560"></td>
</tr>
</table>

Type: Evaluation | Date: 2026-11-19

---

<a id="case-77"></a>
### Case 77: [スプレッドシートでコンピューター ビジョン ラボを構築する](https://www.youtube.com/watch?v=vPsBbuz9IbE) (by [@Google](https://blog.google/))

**スプレッドシートのみのビジュアライゼーションを評価するときに、どの効果が数式から得られるかを検査します。**

Google は、Neon の群れが 1 つの参照画像を 100,000 セルのスプレッドシートに変えたと報告しています。

このデモでは、エッジ検出、深度マッピング、再ライティングなどのタスクに 6 つのモードにわたって 500,000 を超える数式が使用されています。

[補足資料](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/)

<a href="https://www.youtube.com/watch?v=vPsBbuz9IbE"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-77-1-8d819090ab15.jpg" alt="スプレッドシートでコンピューター ビジョン ラボを構築する · 1" width="560"></a>

Type: Demo | Date: 2026-11-18

---

## 📈 評価と限界
<a id="evaluations"></a>

<a id="case-78"></a>
### Case 78: [Vals Index でドメインのパフォーマンスを測定する](https://x.com/ValsAI/status/2123168167879147542) (by [@ValsAI](https://x.com/ValsAI))

**タスクレベルの結果を使用して、集計ランクがドメインと一致するかどうかを確認します。**

Vals AI は、Neon で 70.9% を報告し、Fable 5.2 に 0.4 ポイント差の 2 位の総合順位を記録しました。

この評価者は、財務および法務インデックス、税務代理人および法的調査タスクでも第 1 位を報告します。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-78-1-a072bf0d10fb.jpg" alt="Vals Index でドメインのパフォーマンスを測定する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-79"></a>
### Case 79: [早期アクセス中にインタラクティブなデモをテストする](https://x.com/kimmonismus/status/2123168299890704735) (by [@kimmonismus](https://x.com/kimmonismus))

**成功したプロトタイプと、同じ早期アクセス スレッドで報告された失敗したプロトタイプを比較します。**

著者は、Antigravity で Neon を使用して 17 のインタラクティブなデモを構築し、追加のコーディングとツールのテストを文書化したと報告しています。

公開されたスレッドでは、成功と問題の両方が報告されています。そのデモは、1 つの早期アクセス テスト シリーズとしてグループ化されています。

<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/videos/case-79-1-2c55ce07666c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/posters/case-79-1-d15a99ad1fc4.jpg" alt="早期アクセス中にインタラクティブなデモをテストする · 1" width="560"></a>

Type: Evaluation | Date: 2026-11-18

---

<a id="case-80"></a>
### Case 80: [Agent Arena でエージェント セッションを比較する](https://x.com/arena/status/2123169189397709174) (by [@arena](https://x.com/arena))

**Agent Arena の結果を比較する場合は、報告されたスコアとともにタスクあたりのコストの中央値を使用します。**

Arena の報告では Neon High は 1336 ポイントで 2 位、タスクあたりの費用の中央値は 2.82 米ドルでした。

Arena の投稿によると、評価はコミュニティのエージェントセッション約 4,200 件に基づいています。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-80-1-98fe72255edb.png" alt="Agent Arena でエージェント セッションを比較する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-81"></a>
### Case 81: [Neon を Text Arena に配置](https://x.com/arena/status/2123169199396946279) (by [@arena](https://x.com/arena))

**スコアを読み取るときに、同じアリーナのスナップショットと推論設定を比較します。**

Arena の発表では、Neon High は 1518、Carbon High は 1526、Argon High は 1521 でした。

これは、ベンチマーク発行元からの Text Arena のスナップショットです。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-81-1-c75a9fa2d99d.png" alt="Neon を Text Arena に配置 · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-82"></a>
### Case 82: [Wojak-Benchで3Dプリント用のフィギュアを評価する](https://x.com/lukaspet/status/2123169317076574513) (by [@lukaspet](https://x.com/lukaspet))

**掲載された順位はペア比較の一時点の結果として読み、評価値を引用する前に最新の順位表を確認する。**

ベンチマークの共著者は、Neon が 4 位でデビューしたと報告しました。投稿されたリーダーボードのスナップショットでは、Neon の評価は 1056 です。

各モデルは同じ参考イラストから3Dプリント用のフィギュアを作る。訪問者が2つの出力を比較して投票するため、評価値は票が増えると変わり得る。

[補足資料](https://wojak-bench.dev.pion.dev/)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-82-1-fb8d9cb391a5.jpg" alt="Wojak-Benchで3Dプリント用のフィギュアを評価する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-83"></a>
### Case 83: [コーディング エージェントとそのハーネスを比較する](https://x.com/ArtificialAnlys/status/2123170648772288540) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**コーディング結果を比較するときに、各モデルの評価セットアップと設定を表示したままにします。**

人工分析では、Antigravity CLI を使用した Neon xhigh については 59、Carbon high については 55 が報告されます。

Neon のタスクあたりの平均コストは 6.86 米ドルであると報告されています。ソース内のクロード比較には、クロード コードと別の推論設定を使用しました。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-83-1-ca536c909af6.jpg" alt="コーディング エージェントとそのハーネスを比較する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-84"></a>
### Case 84: [AA-Briefcase でのナレッジ ワークを評価する](https://x.com/ArtificialAnlys/status/2123170651980931421) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**ベンチマークを解釈するときは、プレゼンテーションの品質を全体のスコアから切り離してください。**

人工分析では、Neon xhigh の Elo が 1700、Carbon high の Elo が 1611 と報告されています。

発行者は、Neon のプレゼンテーション スコアとして 1771 を報告しています。リンクされた比較では、パブリック Briefcase-Lite タスクを使用します。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-84-1-b09c2428be07.jpg" alt="AA-Briefcase でのナレッジ ワークを評価する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-85"></a>
### Case 85: [Artificial Analysis Intelligence Index タスクの時間を計測する](https://x.com/ArtificialAnlys/status/2123170655424450840) (by [@ArtificialAnlys](https://x.com/ArtificialAnlys))

**推論設定を選択するときに、トークン出力レートとは別にエンドツーエンド時間を測定します。**

Artificial Analysis の報告では、1 タスクあたりの所要時間は Neon xhigh が約 21 分、Carbon high が約 36 分でした。

発行者は、Neon がより高い出力レートで約 15% 多くの出力トークンを使用したと報告しています。これらの異なる設定では、Neon が 61、Carbon が 60 にランクされました。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-85-1-69e9aff683fe.jpg" alt="Artificial Analysis Intelligence Index タスクの時間を計測する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-86"></a>
### Case 86: [自動販売機ビジネスのシミュレーションを実行する](https://x.com/andonlabs/status/2123174738789011875) (by [@andonlabs](https://x.com/andonlabs))

**エージェントのシミュレーションを判断するときは、トランザクション ログと最終残高を確認してください。**

Andon Labs は、投稿時に Vending-Bench 2 で Neon を最初に報告しました。

そのシミュレーションログには虚偽の交渉の主張が含まれていましたが、報告された実行では捏造された注文紛失や支払い漏れはありませんでした。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-86-1-7dc3cded4337.jpg" alt="自動販売機ビジネスのシミュレーションを実行する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-87"></a>
### Case 87: [RuneScape ベンチマークの制限時間を調べる](https://x.com/maxbittker/status/2123183525515886696) (by [@maxbittker](https://x.com/maxbittker))

**たとえ計画が妥当であるように見えても、タスクの期限を超えた実行は不完全なものとして扱います。**

ベンチマーク作成者は、Neon の野心的な戦略が期限までに完了しなかったと報告しました。

この観察は、この時間制限のある環境に関するものであり、計画の品質と予定どおりの完了に個別のチェックが必要な理由を示しています。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-87-1-e374930df0e2.jpg" alt="RuneScape ベンチマークの制限時間を調べる · 1" width="560">

Type: Limit | Date: 2026-11-18

---

<a id="case-88"></a>
### Case 88: [APEX-Agents で専門的なタスクを実行する](https://x.com/mercor/status/2123184025808650641) (by [@mercor](https://x.com/mercor))

**専門的なタスクを比較するときは、初回試行の合格率と平均スコアを区別してください。**

Mercor は、APEX-Agents の Neon の Pass@1 スコアが 82.9%、平均スコアが 88.9% であると報告しています。

これらは別の指標です。この発行者は、別の APEX-Accounting テストでも 23.5% Pass@1 の結果を報告しています。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-88-1-8c2587fa0e1d.jpg" alt="APEX-Agents で専門的なタスクを実行する · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-89"></a>
### Case 89: [CursorBench 4.1 での Neon と Hydrogen の比較](https://x.com/cursor_ai/status/2123198346802450926) (by [@cursor_ai](https://x.com/cursor_ai))

**同じ CursorBench バージョンを使用し、指定された推論設定でスコアを比較します。**

Cursor は、デフォルトの努力で Neon について 63.7%、Hydrogen について 57.3% を報告します。

この比較は Cursor の評価で実行されたものであり、他のハーネスのパフォーマンスを確立するものではありません。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-89-1-5735136cf3d0.jpg" alt="CursorBench 4.1 での Neon と Hydrogen の比較 · 1" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-90"></a>
### Case 90: [CUDA デバッグ タスクの実時間を測定する](https://x.com/elliotarledge/status/2123200759819124893) (by [@elliotarledge](https://x.com/elliotarledge))

**スループットから結論を引き出す前に、同じデバッグ タスクの実時間を測定してください。**

著者は CUDA デバッグ プロンプトでモデルを実行し、トークン レートとエンドツーエンドの遅延を個別に測定しました。

この結果では、Neon では約 76 秒、Astra と Opus 5.5 では約 20 秒だったと著者は報告しています。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-90-1-1ba56f57fa03.jpg" alt="CUDA デバッグ タスクの実時間を測定する · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-90-2-a4be57aa7260.jpg" alt="CUDA デバッグ タスクの実時間を測定する · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-90-3-93ad692aa067.jpg" alt="CUDA デバッグ タスクの実時間を測定する · 3" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="case-91"></a>
### Case 91: [Tuesday@Work で職場のタスクを測定する](https://x.com/HelloSurgeAI/status/2123213638819348485) (by [@HelloSurgeAI](https://x.com/HelloSurgeAI))

**ドメイン固有の結果を Tuesday@Work 集計とともに使用します。**

Surge AI は評価スイートで Neon を実行し、Tuesday@Work では 71.6 を報告しましたが、Fable 5.2 では 71.2 でした。

この出版社は、DAYJOB Finance、GDP.xlsx、Riemann-bench の上位の順位も報告しています。スコアはテストに適用されます。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-91-1-d95fd2a981f4.png" alt="Tuesday@Work で職場のタスクを測定する · 1" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-92"></a>
### Case 92: [Antigravity でのペナルティ決定を確認する](https://x.com/wenhaocha1/status/2123252530713124967) (by [@wenhaocha1](https://x.com/wenhaocha1))

**同じ評価設定でエージェントの判断を参照判断と比較します。**

Penalty Bench の作成者は、Neon が Antigravity ハーネスを使用したベンチマークで 1 位にランクされたと報告しています。

この情報源では、審判の判定と比較した少数のペナルティ決定について説明しています。その評価の中での結果です。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-92-1-8856d3ed5c45.jpg" alt="Antigravity でのペナルティ決定を確認する · 1" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-93"></a>
### Case 93: [ブラウザ使用ベンチマーク](https://x.com/browser_use/status/2123263050501509123) (by [@browser_use](https://x.com/browser_use))

**ブラウザーのベンチマークと、発行者の評価設定内での実行コストを比較します。**

Browser Use では、Neon の結果が 74% で、Opus 5.5 の結果と同等、GPT-6.2 Sol の 82% と報告されました。

これらのスコアは、出版社のベンチマークを表します。その評価にはコストの比較が適用されます。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-93-1-348151332c55.jpg" alt="ブラウザ使用ベンチマーク · 1" width="560">

Type: Benchmark | Date: 2026-11-19

---

<a id="case-94"></a>
### Case 94: [PandaCode でのツール呼び出しの失敗を測定する](https://x.com/aicodeking/status/2123277076174196882) (by [@aicodeking](https://x.com/aicodeking))

**一致するウィンドウでの失敗を比較し、テスト設定の違いを考慮します。**

著者は、1 回の起動夜のウィンドウで、9,465 回の Neon 呼び出しのうち、65 回の失敗したツール呼び出しを測定しました。

同じ時間帯で、Neon と Carbon の失敗率はいずれも四捨五入で 0.7 % でした。他モデルの大半は、異なる評価環境での全期間の記録です。

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-94-1-95b9a0bbc14d.jpg" alt="PandaCode でのツール呼び出しの失敗を測定する · 1" width="560">

Type: Evaluation | Date: 2026-11-19

---

<a id="case-95"></a>
### Case 95: [43 の質問からなる Plotly データ分析ベンチマークを実行する](https://news.ycombinator.com/item?id=50553968) (by [@chriddyp](https://news.ycombinator.com/user?id=chriddyp))

**同じ Plotly 評価内で、質問ごとの正しさ、コスト、時間の中央値を比較します。**

Plotly の修正結果では、Neon が 43 件中 43 件の回答を獲得し、フル実行で 17.03 米ドルと報告されています。

Hydrogen も 43 問中 43 問に正解し、費用は 6.36 米ドルでした。Plotly が報告した 1 問あたりの所要時間の中央値は、Neon が 46 秒、Hydrogen が 32 秒でした。データ分析向けの評価環境で、各モデルを 1 回ずつ実行した結果です。

[補足資料](https://plotly.com/blog/gemini-4-neon-plotly-data-analytics-bench/)

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-95-1-3c8ca3bdc83b.webp" alt="43 の質問からなる Plotly データ分析ベンチマークを実行する · 1" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-95-2-477010cdc694.webp" alt="43 の質問からなる Plotly データ分析ベンチマークを実行する · 2" width="560">
<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/cheercheung/awesome-gemini-4-neon-use-cases/images/case-95-3-40967c5923ed.webp" alt="43 の質問からなる Plotly データ分析ベンチマークを実行する · 3" width="560">

Type: Benchmark | Date: 2026-11-18

---

<a id="related-repositories"></a>
## 関連リポジトリ

- [Gemini 4 Carbon のガイドと使用例](https://github.com/cheercheung/awesome-gemini-4-carbon-guide-and-use-cases)
- [Gemini 4 水素の使用例](https://github.com/Evolink-AI/awesome-gemini-4-hydrogen-use-cases)

<a id="acknowledge"></a>
## 🙏 謝辞

作品を共有してくれたクリエイターと評価者に感謝します。

[@IndependentEco](https://x.com/IndependentEco), [@SamuelAlbanie](https://x.com/SamuelAlbanie), [@seveibar](https://x.com/seveibar), [@kajikent](https://x.com/kajikent), [@theo](https://x.com/theo), [@Lentils80](https://x.com/Lentils80), [@HarshithLucky3](https://x.com/HarshithLucky3), [@AdamHoltererer](https://x.com/AdamHoltererer), [@StatsWire](https://x.com/StatsWire), [@lyraxana](https://x.com/lyraxana), [@xiangning0](https://x.com/xiangning0), [@Angaisb_](https://x.com/Angaisb_), [@cfenghub](https://x.com/cfenghub), [@kickingkeys](https://x.com/kickingkeys), [@Super_Nius](https://x.com/Super_Nius), [@AI_Screening](https://x.com/AI_Screening), [@Mr_Salio](https://x.com/Mr_Salio), [@LuminaBench](https://x.com/LuminaBench), [@notjazii](https://x.com/notjazii), [@jony_palino](https://x.com/jony_palino), [@thebuggeddev](https://x.com/thebuggeddev), [@GeokenAI](https://x.com/GeokenAI), [@LeslieNooteboom](https://x.com/LeslieNooteboom), [@SPAC89](https://x.com/SPAC89), [@agenticjay](https://x.com/agenticjay), [@Google](https://x.com/Google), [@LyalinDotCom](https://x.com/LyalinDotCom), [@fofrAI](https://x.com/fofrAI), [@thehypedotnews](https://x.com/thehypedotnews), [@chetaslua](https://x.com/chetaslua), [@aipulseda1ly](https://x.com/aipulseda1ly), [@jan_volad](https://x.com/jan_volad), [@ai_for_success](https://x.com/ai_for_success), [@abhinavflac](https://x.com/abhinavflac), [@DesignArena](https://x.com/DesignArena), [@ZryMiller](https://x.com/ZryMiller), [@thtbee_](https://x.com/thtbee_), [@op7418](https://x.com/op7418), [@nemumusitocha](https://x.com/nemumusitocha), [@GoogleAI](https://x.com/GoogleAI), [@antigravity](https://x.com/antigravity), [@GlitterPixely](https://x.com/GlitterPixely), [@badboyfoxy](https://x.com/badboyfoxy), [@DeryaTR_](https://x.com/DeryaTR_), [@Google](https://blog.google/), [@Arcadia_Bao](https://x.com/Arcadia_Bao), [@gracepursuits](https://x.com/gracepursuits), [@Msfs2000J](https://x.com/Msfs2000J), [@viticci](https://x.com/viticci), [@tetumemo](https://x.com/tetumemo), [@MichaelLee009](https://x.com/MichaelLee009), [@ValsAI](https://x.com/ValsAI), [@kimmonismus](https://x.com/kimmonismus), [@arena](https://x.com/arena), [@lukaspet](https://x.com/lukaspet), [@ArtificialAnlys](https://x.com/ArtificialAnlys), [@andonlabs](https://x.com/andonlabs), [@maxbittker](https://x.com/maxbittker), [@mercor](https://x.com/mercor), [@cursor_ai](https://x.com/cursor_ai), [@elliotarledge](https://x.com/elliotarledge), [@HelloSurgeAI](https://x.com/HelloSurgeAI), [@wenhaocha1](https://x.com/wenhaocha1), [@browser_use](https://x.com/browser_use), [@aicodeking](https://x.com/aicodeking), [@chriddyp](https://news.ycombinator.com/user?id=chriddyp)

*メディアおよびサードパーティの著作物は、それぞれの権利所有者に帰属します。ソース、クレジット、またはメディア アイテムに修正が必要な場合は、問題を開いてください。*
