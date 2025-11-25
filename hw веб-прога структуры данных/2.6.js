const subjects = {
    list: "Математика,Физика,Информатика",
    add(subj) {
        let arr = this.list.split(',');
        if (!arr.includes(subj)) {
            arr.push(subj);
            this.list = arr.join(',');
        }
    },
    remove(subj) {
        let arr = this.list.split(',');
        let idx = arr.indexOf(subj);
        if (idx !== -1) {
            arr.splice(idx, 1);
            this.list = arr.join(',');
        }
    }
};

subjects.add('Английский');
subjects.remove('Физика');
console.log(subjects.list); // "Математика,Информатика,Английский"