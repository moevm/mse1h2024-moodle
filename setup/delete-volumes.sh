volumes=$(docker inspect --format='{{json .Mounts}}' mongodb | grep -o '"Name":"[^"]*' | grep -o '[^"]*$')

docker rm --force mongodb

for volume in $volumes; do
    echo "Удаление volume: $volume"
    docker volume rm "$volume"
done

echo "Volumes успешно очищены."