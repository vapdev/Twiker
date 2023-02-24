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