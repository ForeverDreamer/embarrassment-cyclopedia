import {Component, Input, OnInit} from '@angular/core';
import { IndexItem } from './index-item.model';

@Component({
  selector: 'app-index-item',
  templateUrl: './index-item.component.html',
  styleUrls: ['./index-item.component.scss'],
})
export class IndexItemComponent implements OnInit {
  @Input() item: IndexItem;

  constructor() { }

  ngOnInit() {}

}
