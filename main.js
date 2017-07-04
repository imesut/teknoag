for (var i = 0; i < 21; i++) {
	loadMore()
};

var links = document.getElementsByTagName("a")

var linklist = ""

for (i in links){
	linklist += links[i].href+"<br>";
}

var blob = new Blob([linklist], {type: "text/plain;charset=utf-8"});
var blobUrl = URL.createObjectURL(blob);
var downloadLink = document.createElement("a");
downloadLink.href = blobUrl;
downloadLink.download = "links.py";
downloadLink.innerHTML = "Download company links here.";
document.body.appendChild(downloadLink);