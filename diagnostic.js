function outputTable(rows, cols) {
    const lastRowLen = [];
    const resRows = [];

    for (let i = rows; i > 0; i--) {
        const currentRows = [];
        for (let j = 1; j <= cols; j++) {
            if (i === rows) lastRowLen.push((j * i).toString().length);
            currentRows.push(j * i);
        }
        resRows.push(currentRows);
    }
    resRows.reverse();

    for (let i = 0; i < rows; i++) {
        let resString = "";
        const row = resRows[i];
        for (let j = 0; j < row.length; j++) {
            const offset = lastRowLen[j] - row[j].toString().length;
            resString = resString + " ".repeat(offset + 2) + row[j];
        }
        console.log(resString);
    }
}

outputTable(10, 11);
