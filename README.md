# ytcapture

## 用途
利用 youtube-dl 查詢串流內容 再使用 ffmpeg 進行間隔下載影像視訊匡(video frame)  連續點擊畫面可以直接儲存該視訊框

## 依賴
* Pillow
* NumPy
* PyQt5
* ffmpeg
* youtube-dl

## 使用方式
* Python -
1. 原始碼下載後 建立 venv (避免搞砸你的原來工作環境) 利用 pip install -r requirements.txt 安裝需要的 python package
2. 下載 ffmpeg static 版本 - 解壓縮後放入目錄內 windows link (https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20190421-6e0488c-win64-static.zip)
3. 如果需要修改 拉取視訊框的 『時間間隔』 與 『頻道設定』， 請直接修改 settings.json 裡面的 interval 與 channels 兩個項目即可

* Windows PreBuild 執行檔 - 改用 pyinstaller 靜態化
1. https://www.dropbox.com/s/spydypyr9hhfrl6/ytcapture_20190425.zip?dl=0  把預先編譯靜態化的執行檔(windows only - windows 7 and windows 10 測試 OK)

* 直接雙擊畫面會把截圖儲存到使用者桌面目錄
* 畫面下方有選單可以選擇目前預設的 youtube 新聞頻道
* 利用 sparse-checkout 只同步 yotube-dl/yotube_dl 子目錄
<pre><code>
    git init youtube_dl
    cd youtube_dl
    git config core.sparsecheckout true
    echo youtube_dl/* >> .git/info/sparse-checkout
    git remote add origin https://github.com/ytdl-org/youtube-dl
    git pull origin master
</code></pre>