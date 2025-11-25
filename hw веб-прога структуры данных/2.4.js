const week = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота',
    7: 'Воскресенье',
    today() {
        let num = new Date().getDay(); // 0-Вс, 1-Пн,...
        num = num === 0 ? 7 : num; // Вс=7
        return this[num];
    }
};

console.log('Сегодня:', week.today());