function translate(str, lang) {
    const dict = {
        hello:   {en: 'hello', ru: 'привет', fr: 'bonjour'},
        dog:     {en: 'dog', ru: 'собака', fr: 'chien'},
        cat:     {en: 'cat', ru: 'кот', fr: 'chat'},
        thanks:  {en: 'thanks', ru: 'спасибо', fr: 'merci'},
    };
    return dict[str] && dict[str][lang] ? dict[str][lang] : 'Нет перевода';
}

console.log(translate('hello', 'ru')); // привет
console.log(translate('thanks', 'fr')); // merci