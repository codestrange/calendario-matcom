export const renderPresentation = function (_start, _end) {
    let start = new Date(_start);
    let end = new Date(_end);
    start.setHours(start.getHours() + 4);
    end.setHours(end.getHours() + 4);
    var result = '';
    if (equalDate(start, end)) {
        result += 'El ' + renderDay(start) + ' ' + renderDate(start);
        result += ' desde ' + renderPrefix(start) + ' ';
        result += renderTime(start) + ' hasta ' + renderPrefix(end);
        result += ' ' + renderTime(end) + '.';
    } else {
        result += 'El ' + renderDay(start) + ' ' + renderDate(start);
        result += ' desde ' + renderPrefix(start) + ' ';
        result += renderTime(start) + ' hasta el ';
        result += renderDay(end) + ' ' + renderDate(end) + ' a ';
        result += renderPrefix(end) + ' ' + renderTime(end) + '.';
    }
    return result;
}

function renderPrefix(datetime) {
    var result = 'la';
    var hours = datetime.getHours();
    if (hours != 1 && hours != 13)
        result += 's';
    return result;
}

function renderDay(datetime) {
    var days = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];
    return days[datetime.getDay()];
}

function renderTime(datetime) {
    var result = '';
    var hours = datetime.getHours();
    if (hours == 0)
        hours += 12;
    if (hours > 12)
        hours -= 12;
    if (hours < 10)
        result += '0';
    result += hours + ':';
    if (datetime.getMinutes() < 10)
        result += '0';
    result += datetime.getMinutes();
    if (datetime.getHours() < 12)
        result += ' AM';
    else
        result += ' PM';
    return result;
}

function renderDate(datetime) {
    var result = '';
    if (datetime.getDate() < 10)
        result += '0';
    result += datetime.getDate() + '/';
    if (datetime.getMonth() < 10)
        result += '0';
    result += (datetime.getMonth() + 1) + '/' + datetime.getFullYear();
    return result;
}

function equalDate(a, b) {
    if (a.getDate() == b.getDate())
        if (a.getMonth() == b.getMonth())
            if (a.getFullYear() == b.getFullYear())
                return true;
    return false;
}