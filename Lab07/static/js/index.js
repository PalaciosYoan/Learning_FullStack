const url = "http://127.0.0.1:5000/grade";

function APIget(x = "", meth = "GET") {
    let newQuery;
    if (x === "") {
        newQuery = url;
    } else {
        x = `${x}`.split(" ");
        if (x.length > 1) newQuery = url + `/${x[0]}%20${x[1]}`;
        else newQuery = url + `/${x[0]}`;
    }
    console.log(newQuery);
    fetch(newQuery, {
            method: meth,
        })
        .then((res) => {
            if (res.ok) {
                return res.json();
            }
        })
        .then((res) => {
            const html = res;
            let text = "";
            for (key in html) {
                text += "<tr><td>" + key + "</td><td>" + html[key] + "</td></tr>";
            }
            text += "</table>";
            document.getElementById("tableAllGrades").innerHTML = text;
            // document.getElementById("allgrades").textContent = JSON.stringify(
            //     html,
            //     undefined,
            //     2
            // );
        });
}

function APIpost(name, grade, meth) {
    let newQuery = url;

    fetch(newQuery, {
            method: meth,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
                grade: parseFloat(grade),
            }),
        })
        // 404 Error check
        .then((res) => {
            if (res.ok) {
                console.log("Posted");
                return res.json();
            } else {
                console.log("Failed");
                return Promise.reject(res.status);
            }
        })
        //.then((res) => console.log(res))
        .catch((err) => console.log(`Error with message: ${err}`));
}

function APIput(name, grade, meth) {
    let newQuery;
    if (name === "") {
        newQuery = url;
    } else {
        x = `${name}`.split(" ");
        if (x.length > 1) newQuery = url + `/${x[0]}%20${x[1]}`;
        else newQuery = url + `/${x[0]}`;
    }
    fetch(newQuery, {
            method: meth,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                name: name,
                grade: grade,
            }),
        })
        // 404 Error check
        .then((res) => {
            if (res.ok) {
                console.log("Posted");
                return res.json();
            } else {
                console.log("Failed");
                return Promise.reject(res.status);
            }
        })
        //.then((res) => console.log(res))
        .catch((err) => console.log(`Error with message: ${err}`));
}

APIget();

function refresh() {
    APIget();
}

const btn1 = document.getElementById("1");
btn1.addEventListener("click", () => {
    let y = document.getElementById("studentnameget").value;
    document.getElementById("studentnameget").value = "";
    APIget(y);
});

const btn2 = document.getElementById("allinfo");
btn2.addEventListener("click", () => {
    APIget();
});

const btn3 = document.getElementById("2");
btn3.addEventListener("click", () => {
    let name = document.getElementById("studentname").value;
    let grade = document.getElementById("studentgrade").value;

    document.getElementById("studentname").value = "";
    document.getElementById("studentgrade").value = "";

    APIpost(name, grade, "POST");
});

const btn4 = document.getElementById("3");
btn4.addEventListener("click", () => {
    let name = document.getElementById("studentname1").value;
    let grade = document.getElementById("studentgrade1").value;
    document.getElementById("studentname1").value = "";
    document.getElementById("studentgrade1").value = "";

    APIput(name, grade, "PUT");
});

const btn5 = document.getElementById("4");
btn5.addEventListener("click", () => {
    let name = document.getElementById("studentname2").value;
    APIget(name, "DELETE");
});