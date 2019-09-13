import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { IndexPage } from './index.page';
import { IndexItemComponent } from '../components/index-item/index-item.component';
import { NavTabComponent } from '../components/nav-tab/nav-tab.component';


const routes: Routes = [
  {
    path: '',
    component: IndexPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [IndexPage, IndexItemComponent, NavTabComponent]
})
export class IndexPageModule {}
