const staff = {
    директор: 'Иванов',
    учитель: 'Петрова',
    секретарь: 'Сидорова',
};

const staff2 = {...staff, директор: 'Смирнов', учитель: 'Кузнецова', секретарь: 'Андреева'};

function objToStr(obj) {
    return Object.entries(obj)
        .map(([k, v]) => `${k}: ${v}`)
        .join('\n');
}
console.log('Персонал 1:\n' + objToStr(staff));
console.log('\nПерсонал 2:\n' + objToStr(staff2));