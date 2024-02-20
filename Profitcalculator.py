from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    original_html = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profit Calculator</title>
</head>
<body>
    <h1>Profit Calculator</h1>
    <form id="profitForm">
        <label for="purchasePrice">Purchase Price:</label>
        <input type="number" id="purchasePrice" name="purchasePrice" required><br><br>

        <label for="profitRate">Profit Rate (%):</label>
        <input type="number" id="profitRate" name="profitRate" required><br><br>

        <button type="button" onclick="calculateProfit()">Calculate Profit</button>
    </form>

    <div id="result"></div>

    <script>
        function calculateProfit() {
            var purchasePrice = parseFloat(document.getElementById('purchasePrice').value);
            var profitRate = parseFloat(document.getElementById('profitRate').value);

            var profit = purchasePrice * (profitRate / 100);
            var total = purchasePrice + profit;

            document.getElementById('result').innerHTML = "Profit: $" + profit.toFixed(2) + "<br>Total: $" + total.toFixed(2);
        }
    </script>
</body>
</html>

    """

    return render_template_string(original_html)

if __name__ == '__main__':
    app.run(debug=True)