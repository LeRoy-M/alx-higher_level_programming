#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  // 'charPrint()' Instance Method
  charPrint (chr) {
    if (chr === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let shp = '';
        for (let j = 0; j < this.width; j++) {
          shp += chr;
        }
        console.log(shp);
      }
    }
  }
};
