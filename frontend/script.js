function startScan() {
    const url = document.getElementById("url").value.trim();
    if (!url) return (document.getElementById("status").textContent = 'Please enter a URL');

    document.getElementById("status").innerHTML = "🔍 Scanning...";

    fetch("http://127.0.0.1:5000/api/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
        .then(async res => {
            if (!res.ok) throw new Error(`${res.status} ${res.statusText}`);
            return res.json();
        })
        .then(data => {
            localStorage.setItem("scan_response", JSON.stringify(data));
            window.location.href = "result.html";
        })
        .catch(err => {
            document.getElementById("status").textContent = 'Scan failed: ' + err.message;
        });
}

window.onload = function() {
    const box = document.getElementById("result");
    if (!box) return;

    const raw = localStorage.getItem("scan_response");
    if (!raw) return (box.textContent = 'No results available.');

    try {
        const data = JSON.parse(raw);
        box.innerHTML = `<h3>Scan ID: ${data.scan_id || 'N/A'}</h3><pre>${JSON.stringify(data.result || data, null, 2)}</pre>`;
    } catch (e) {
        box.textContent = 'Failed to parse stored result.';
    }
}
