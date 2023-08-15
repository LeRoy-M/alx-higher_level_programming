#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // 'print()' Instance Method
  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let j = 0; j < this.width; j++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  // 'rotate()' Instance Method
  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // 'double()' Instance Method
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
