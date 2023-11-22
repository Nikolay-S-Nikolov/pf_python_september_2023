some_dict = {"mp3": ["song1", "song2", "song3"],
             "mp4": ["song1", "song2"],
             "video": ["song1", "song2"]}

for key in some_dict.keys():
    print(key)
for value in some_dict.values():
    print(value)
for key,value in some_dict.items():
    print(f"key = '{key}', Value = '{value}'")
