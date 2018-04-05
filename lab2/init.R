library("XML")

path = "nyt_corpus/samples_500/"
fileList = list.files(path)

search = function (node, attrs){
	name = xmlName(node)
	size = xmlSize(node)
	if (name == "meta") {
		if (xmlGetAttr(node, "name") == "publication_year") attrs[[1]] = xmlGetAttr(node, "content")
		if (xmlGetAttr(node, "name") == "publication_month") attrs[[2]] = xmlGetAttr(node, "content")
		if (xmlGetAttr(node, "name") == "publication_day_of_month") attrs[[3]] = xmlGetAttr(node, "content")
	}

	if (name == "classifier") {
		tagList = (strsplit(xmlValue(node), "/"))
		if (length(tagList[[1]]) > 2 && tagList[[1]][[1]] == "Top" && (tagList[[1]][[2]] == "News" || tagList[[1]][[2]] == "Features")) {
			flag = FALSE
			for (i in attrs[[4]]) {
				if (i == tagList[[1]][[3]]) flag = true
			
			}
			print(class(tagList[[1]][[3]]))
			if (!flag) attrs[[4]] = c(attrs[[4]], tagList[[1]][[3]])
			print(attrs[[4]])
		}
	}

	if (name == "block" && xmlGetAttr(node, "class") == "full_text") {
		attrs[[5]] = ""
		for (i in 1 : size) attrs[[5]] = paste(attrs[[5]], xmlValue(node[[i]][[1]]), sep = " ")
		return(attrs)
	}
	if (size > 0) for (i in 1 : size) attrs = search(node[[i]], attrs)
	return(attrs)
}


inst = xmlParse(file = paste(path, fileList[1], sep = ""))
node = xmlRoot(inst)

tagList = vector(mode = "character", length = 0)

attrs = c("", "", "", tagList, "")

attrs = search(node, attrs)
print(attrs[[4]])
date = paste(attrs[[1]], attrs[[2]], attrs[[3]], sep = "-")
