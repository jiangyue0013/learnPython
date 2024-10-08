try:
    x = 10
    print(x)
except NameError:
    print("Variable x is not defined!")
except:
    print("Something else went wrong!")
else:
    print("Nothing went wrong.")
finally:
    print("The 'try except is finished.")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writting to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")

# x = -1
# if x < 0:
#     raise Exception("Sorry, no numbers below zero!")

x = "hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed!")
