import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { EmbarrassmentPage } from './embarrassment.page';
import { EmbarrassmentRoutingModule } from './embarrassment-routing.module';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    EmbarrassmentRoutingModule
  ],
  declarations: [EmbarrassmentPage]
})
export class EmbarrassmentPageModule {}
