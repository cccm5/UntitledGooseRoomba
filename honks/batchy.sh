for i in *.mp3;
  do name=`echo "$i" | cut -d'.' -f1`
  echo "$name"
  xdg-open "${name}.mp3"
done

