ctarget = "#target1"
dtarget = "#target2  #target3"

target = ctarget
target = target.split(" ")
target = {t.replace("#", ""):t.strip() for t in target if t.strip() != ""}
print(target)