import {Component, OnInit} from '@angular/core';
import {IndexItem, InfoNum} from '../components/index-item/index-item.model';

@Component({
    selector: 'app-index',
    templateUrl: './index.page.html',
    styleUrls: ['./index.page.scss'],
})
export class IndexPage implements OnInit {
    items: IndexItem[];

    constructor() {
    }

    ngOnInit() {
        this.items = [
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
    }

}
