time=`date "+%Y_%m_%d_%H_%M"`
mkdir -p "./data/$time"
i=0
while : ;do
	tail=".jpg"
	img_name="./data/${time}/frame_${i}${tail}"
	raspistill -o ${img_name}
	echo $img_name
	i=$(($i+1))
done
