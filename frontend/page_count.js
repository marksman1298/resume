function getCount() {
    let api_url = "https://kt73w1yzv9.execute-api.ca-central-1.amazonaws.com/dev/page_count"
    fetch(api_url)
    .then((response) => response.json())
    .then((response) => (document.getElementById("views")).innerHTML = response.body);
}