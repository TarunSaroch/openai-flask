from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_KEY"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prompt = request.json.get("prompt")
        response = openai.Completion.create(
            model="text-davinci-003", prompt=prompt, temperature=0.7, max_tokens=50
        )
        text = response["choices"][0]["text"]
        return jsonify({"response": text})
    return """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="icon" href="data:,">
    <script>
    function sendData(){
        event.preventDefault();
        var prompt = document.getElementById("prompt").value;
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var json = JSON.parse(xhr.responseText);
                document.getElementById("response").innerHTML = json.response;
            }
        };
        var data = JSON.stringify({"prompt": prompt});
        xhr.send(data);
    }
    </script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
    body{
    background: url('https://images.unsplash.com/photo-1614850523011-8f49ffc73908?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80');
    background-repeat: no-repeat;
    background-size: cover;
    }
    .header {
      margin: 5% 18%;
      text-align: center;
      height: 750px;
      padding-top: 50px;
      background-color: rgba(255,255,255,0.13);
      border-radius: 25px;

      
      backdrop-filter: blur(10px);
      border: 2px solid rgba(255,255,255,0.1);
      box-shadow: 0 0 40px rgba(8,7,16,0.6);
    }
    #response{
      color: white;
    }
    form {
      display: inline-block;
      width: 70%;
      margin: 0 auto;
      text-align: center;
      position: relative;
    }
    
    input[type="text"] {
      width: 80%;
      height: 60px;
      padding: 12px 20px;
      margin: 8px 0;
      box-sizing: border-box;
      border: 2px solid #ccc;
      border-radius: 15px;
      font-size: 20px;
      margin-right: 20px;
    }
    
    button[type="submit"] {
      width: 90px;
      height: 60px;
      background-color: rgb(7, 43, 205);
      color: white;
      /* padding: 14px 20px; */
      margin: 8px 0;
      font-size: 20px;
      border: none;
      border-radius: 15px;
      cursor: pointer;
    }
    
    button[type="submit"]:hover {
      background-color: #87CEEB;
    }
    .res{
        /* border: solid #87CEEB; */
        margin: 50px;
        margin-top: 20px;
        padding: 10px;
        height: 70%;
        color: white;
        font-size: 25px;
        text-align: left;
        
    }

  </style>
    </head>
    <body>
    <div class="header">
    <form>
    <input type="text" placeholder="Ask me something ..." id="prompt">
    <button type="submit" onclick="sendData()">Search</button>
    </form>
    <div id="response" class="res"></div>
    </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
