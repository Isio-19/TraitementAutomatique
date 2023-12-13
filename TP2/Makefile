all: 
	python3 dict.py
	cd liblinear && make
	./liblinear/train -c 4 -e 0.1 -q svm/train.svm output/tweet.model
	./liblinear/predict svm/test.svm output/tweet.model output/out.txt