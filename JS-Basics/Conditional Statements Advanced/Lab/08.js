function getTicketPrice(day) {
    const ticketPrices = {
        Monday: 12,
        Tuesday: 12,
        Wednesday: 14,
        Thursday: 14,
        Friday: 12,
        Saturday: 16,
        Sunday: 16
    };

    const price = ticketPrices[day];

    console.log(price);

}
