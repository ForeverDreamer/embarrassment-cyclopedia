import {Component, OnInit, ViewChild} from '@angular/core';

import {IonSlides} from '@ionic/angular';

import {IndexItem, InfoNum} from '../components/index-item/index-item.model';

@Component({
    selector: 'app-index',
    templateUrl: './index.page.html',
    styleUrls: ['./index.page.scss'],
})
export class IndexPage implements OnInit {
    private items1: IndexItem[];
    private items2: IndexItem[];
    private items3: IndexItem[];
    private items4: IndexItem[];
    @ViewChild('slides', {static: false}) slides: IonSlides;

    constructor() {
    }

    ngOnInit() {
        this.items1 = [
            new IndexItem(
                '../../../assets/image/userpic/12.jpg',
                '卤大湿',
                true,
                '走出去，才发现你跟别人差得不是一点半点',
                'img',
                new InfoNum(1, 570, 2),
                21,
                14,
                '../../../assets/image/datapic/11.jpg'
            ),
            new IndexItem(
                '../../../assets/image/userpic/12.jpg',
                '小花生不上课',
                false,
                'Python骚操作-自动抢火车票',
                'video',
                new InfoNum(2, 396, 18),
                73,
                45,
                '../../../assets/image/datapic/11.jpg',
                20,
                '2:47'
            ),
        ];
        this.items2 = [
            new IndexItem(
                '../../../assets/image/userpic/12.jpg',
                '卤大湿',
                true,
                '走出去，才发现你跟别人差得不是一点半点',
                'img',
                new InfoNum(1, 570, 2),
                21,
                14,
                '../../../assets/image/datapic/11.jpg'
            ),
            new IndexItem(
                '../../../assets/image/userpic/12.jpg',
                '小花生不上课',
                false,
                'Python骚操作-自动抢火车票',
                'video',
                new InfoNum(2, 396, 18),
                73,
                45,
                '../../../assets/image/datapic/11.jpg',
                20,
                '2:47'
            ),
        ];
        this.items3 = [
            new IndexItem(
                '../../../assets/image/userpic/12.jpg',
                '卤大湿',
                true,
                '走出去，才发现你跟别人差得不是一点半点',
                'img',
                new InfoNum(1, 570, 2),
                21,
                14,
                '../../../assets/image/datapic/11.jpg'
            ),
            new IndexItem(
                '../../../assets/image/userpic/12.jpg',
                '小花生不上课',
                false,
                'Python骚操作-自动抢火车票',
                'video',
                new InfoNum(2, 396, 18),
                73,
                45,
                '../../../assets/image/datapic/11.jpg',
                20,
                '2:47'
            ),
        ];
        this.items4 = [];
    }

    loadData(event, slideInx) {
        setTimeout(() => {

            this.slides.getActiveIndex().then(
                (idx) => {
                    if (slideInx === idx) {
                        console.log('slide ' + idx);
                        switch (idx) {
                            case 0:
                                this.items1.push(new IndexItem(
                                    '../../../assets/image/userpic/12.jpg',
                                    '小花生不上课',
                                    false,
                                    'Python骚操作-自动抢火车票',
                                    'video',
                                    new InfoNum(2, 396, 18),
                                    73,
                                    45,
                                    '../../../assets/image/datapic/11.jpg',
                                    20,
                                    '2:47'
                                ));
                                break;
                            case 1:
                                this.items2.push(new IndexItem(
                                    '../../../assets/image/userpic/12.jpg',
                                    '小花生不上课',
                                    false,
                                    'Python骚操作-自动抢火车票',
                                    'video',
                                    new InfoNum(2, 396, 18),
                                    73,
                                    45,
                                    '../../../assets/image/datapic/11.jpg',
                                    20,
                                    '2:47'
                                ));
                                break;
                            default:
                                this.items3.push(new IndexItem(
                                    '../../../assets/image/userpic/12.jpg',
                                    '小花生不上课',
                                    false,
                                    'Python骚操作-自动抢火车票',
                                    'video',
                                    new InfoNum(2, 396, 18),
                                    73,
                                    45,
                                    '../../../assets/image/datapic/11.jpg',
                                    20,
                                    '2:47'
                                ));
                                break;
                        }

                    }
                });


            event.target.complete();

            // App logic to determine if all data is loaded
            // and disable the infinite scroll
            // if (this.items.length === 10) {
            //     event.target.disabled = true;
            // }
        }, 1000);
    }

}
