var dic=[
    {
        "rollno": "10",
        "name": "Aryan",
        "subject": "java",
        "storage": "Cookies"
    },
    {
        "rollno": "14",
        "name": "Amit",
        "subject": "lihw oivhyiou",
        "storage": "Cookies"
    },
    {
        "rollno": "16",
        "name": "@",
        "subject": "python",
        "storage": "Local"
    },
    {
        "rollno": "12",
        "name": "Unckon",
        "subject": "jgfkjdgk",
        "storage": "Session"
    }
]
// function Delete(num){
//     for (var i in dic){
//         if (i==num){
//             dic.splice(i,i)
//         }
//     }
//     return dic
// }
// console.log(Delete(3))


function Delete(num){
    for (var i in dic){
        if (i==num){
            dic[i]["name"]="niya"
        }
    }
    return dic
}
console.log(Delete(1))