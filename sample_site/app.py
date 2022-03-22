from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/result")
def index():

    # Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()

    # Increment the count 
    count += 1

    # Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    # Render HTML with milestone variables
    if count % 1000 == 0:
        return render_template("index.html", massivemilestone=count, count=count)

    if count % 100 == 0:
        return render_template("index.html", hugemilestone=count, count=count)

    if count % 50 == 0:
        return render_template("index.html", bigmilestone=count, count=count)

    if count % 25 == 0:
        return render_template("index.html", milestone=count, count=count)

    # Render HTML with count variable
    return render_template("index.html", count=count)


if __name__ == "__main__":
    app.run()
