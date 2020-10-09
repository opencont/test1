var n = parseInt(readline());
var cards = readline().split(' ');
 
for (var i = 0; i < n; i++) {
  cards[i] = parseInt(cards[i]);
}
 
var sereja = 0;
var dima = 0;
var turn = 0;
 
while (cards.length > 0) {
  if (turn % 2 == 0) {
    if (cards[0] > cards[cards.length - 1]) {
      sereja += cards[0];
      cards.splice(0, 1);
    } else {
      sereja += cards[cards.length - 1];
      cards.splice(cards.length - 1, 1);
    }
  } else {
    if (cards[0] > cards[cards.length - 1]) {
      dima += cards[0];
      cards.splice(0, 1);
    } else {
      dima += cards[cards.length - 1];
      cards.splice(cards.length - 1, 1);
    }
  }
 
  turn++;
}
 
print(sereja, dima);
