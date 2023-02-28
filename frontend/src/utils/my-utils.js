export function formatted_time(time) {
    const postTime = new Date(time);
    const currentTime = new Date();
    const diffSeconds = Math.floor((currentTime - postTime) / 1000);

    if (diffSeconds < 60) {
        return "há menos de um minuto.";
    } else if (diffSeconds < 3600) {
        const diffMinutes = Math.floor(diffSeconds / 60);
        return `há ${diffMinutes} minuto${diffMinutes > 1 ? "s" : ""}.`;
    } else if (diffSeconds < 86400) {
        const diffHours = Math.floor(diffSeconds / 3600);
        return `há ${diffHours} hora${diffHours > 1 ? "s" : ""}.`;
    } else {
        const diffDays = Math.floor(diffSeconds / 86400);
        return `há ${diffDays} dia${diffDays > 1 ? "s" : ""}.`;
    }
}

export function formatDatetimeCustom(datetimeString) {
    const date = new Date(datetimeString);
    const year = date.getFullYear();
    const month = date.getMonth() + 1;
    const day = date.getDate();
    const hour = date.getHours();
    const minute = date.getMinutes();
    return `${padZero(day)}/${padZero(month)}/${year} ${padZero(hour)}:${padZero(minute)}`;
}

export function formatMonthYear(dateString) {
    const date = new Date(dateString);
    const monthNames = [
      "janeiro", "fevereiro", "março",
      "abril", "maio", "junho", "julho",
      "agosto", "setembro", "outubro",
      "novembro", "dezembro"
    ];
    const month = monthNames[date.getMonth()];
    const year = date.getFullYear();
    return `${month} de ${year}`;
}
  