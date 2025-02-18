function solve() {

    const headers = document.querySelectorAll("thead input[type='checkbox']");
 
    const selectedColumns = [];
    headers.forEach((checkbox, index) => {
        if (checkbox.checked) {
            selectedColumns.push({ index, name: checkbox.getAttribute("name") });
        }
    });

    const rows = document.querySelectorAll("tbody tr");
    const report = [];

    rows.forEach(row => {
        const rowData = {};
        const cells = row.querySelectorAll("td");

        selectedColumns.forEach(column => {
            rowData[column.name] = cells[column.index].textContent.trim();
        });

        report.push(rowData);
    });

    const output = document.querySelector("#output");
    output.value = JSON.stringify(report);
}
