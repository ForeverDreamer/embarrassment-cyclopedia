import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EmbarrassmentPage } from './embarrassment.page';


const routes: Routes = [
    {
        path: 'tabs',
        component: EmbarrassmentPage,
        children: [
            {
                path: 'index',
                loadChildren: './index/index.module#IndexPageModule'
            },
            {
                path: 'news',
                loadChildren: './news/news.module#NewsPageModule'
            },
            {
                path: 'paper',
                loadChildren: './paper/paper.module#PaperPageModule'
            },
            {
                path: 'home',
                loadChildren: './home/home.module#HomePageModule'
            },
            {
                path: '',
                redirectTo: '/embarrassment/tabs/index',
                pathMatch: 'full'
            }
        ]
    },
    {
        path: '',
        redirectTo: '/embarrassment/tabs/index',
        pathMatch: 'full'
    }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class EmbarrassmentRoutingModule {

}
