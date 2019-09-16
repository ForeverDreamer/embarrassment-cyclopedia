import { Component, Input, OnInit } from '@angular/core';

import { ToastController } from '@ionic/angular';

import { IndexItem } from './index-item.model';

@Component({
  selector: 'app-index-item',
  templateUrl: './index-item.component.html',
  styleUrls: ['./index-item.component.scss'],
})
export class IndexItemComponent implements OnInit {
  @Input() item: IndexItem;

  constructor(private toastCtrl: ToastController) { }

  ngOnInit() {}

  // 关注
  async onGuanzhu() {
    this.item.isGuanzhu = true;
    const toast = await this.toastCtrl.create({
      message: '关注成功',
      position: 'middle',
      animated: true,
      cssClass: 'my-toast',
      duration: 2000
    });
    await toast.present();
  }

  // 顶踩
  onCaozuo(type: string) {
    console.log(type);
    switch (type) {
      case 'ding':
        if ( this.item.infoNum.index === 1 ) { return; }
        this.item.infoNum.dingNum++;
        if ( this.item.infoNum.index === 2 ) {
          this.item.infoNum.caiNum--;
        }
        this.item.infoNum.index = 1;
        break;
      case 'cai':
        if ( this.item.infoNum.index === 2 ) { return; }
        this.item.infoNum.caiNum++;
        if ( this.item.infoNum.index === 1 ) {
          this.item.infoNum.dingNum--;
        }
        this.item.infoNum.index = 2;
        break;
      default:
        break;
    }
  }

  // 进入详情页
  openDetail() {
    console.log('进入详情页');
  }
}
