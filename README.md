## m3u-file-collector

sometimes you have a playlist and you want to collect all tracks in a folder, but if files in playlist placed in seperate folders collecting them take a lot of time if you want do this by hand. 
But by this simple python script you can copy all files in your playlist to a folder

####how to use : 
first you have to export your playlist as a [m3u](https://en.wikipedia.org/wiki/M3U) file

```
$ python m3u-file-collector.py <playlist.m3u> <destination>
```

- first argument must be a m3u file.
- second argument is optional. if you don't set it , all files copy in current directory

##### thanks
thanks for [200-sucess](http://codereview.stackexchange.com/users/9357/200-success) [reviews](http://codereview.stackexchange.com/questions/107834/m3u-file-collector) 

